import re
import aiohttp
from config import item_ids
import asyncio
from bs4 import BeautifulSoup
from helper import extract_guild_name, get_item_from_id
from db_commands import insert_char_inventories

async def inventory_scrape(char_name: str) -> None:
    char_url = "https://rotpvp.com/magelo/index.php?page=character&char=" + char_name
    char_inventory = []
    async with aiohttp.ClientSession() as session:
        async with session.get(char_url) as response:
            if response.status == 200:
                try:
                    text = await response.text()
                except UnicodeDecodeError:
                    text = await response.text(encoding='latin-1')
                soup = BeautifulSoup(text, 'html.parser')
                try:
                    guild_name = ''
                    main_element = soup.find("main")
                    for element in main_element.find_all("div"):
                        item = []
                        item_name = ''
                        item_location = ''
                        # Look for guild name
                        if not guild_name:
                            guild_name = extract_guild_name(element)
                        if element.has_attr("id") and "slot" in element["id"]:
                            slot_number = int(element["id"].split("slot")[1])
                            # Determine item location based on the slot number
                            item_location = "Inventory" if slot_number < 2000 else "Bank"
                            item_name_a = element.find_next("a")
                            if item_name_a:
                                item_name = item_name_a.text
                                if item_name:
                                    item_id = item_name_a.get('href')
                                    match = re.search(r'id=(\d+)$', item_id)
                                    if match:
                                        int_val = match.group(1)
                                        # Look for ambigous item ids, so that we can properly name them
                                        if int_val in item_ids:
                                            print('MATCH FOUND')
                                            item_name = get_item_from_id(int_val)
                                            print(item_name)
                                    next_element = element.find_next("div", class_="slotlocinspect")
                                    child_span = next_element.find_next("span")
                                    item.append(char_name)
                                    item.append(item_name)
                                    if child_span.text:
                                        item.append(child_span.text)
                                    else:
                                        item.append(1)
                                    item.append(item_location)
                        item.append(guild_name)
                        if len(item) == 5:
                            char_inventory.append(item)
                    insert_char_inventories(char_inventory)
                    print(f"bulk insert performed for: {char_name}")
                    
                except:
                    print("FAILED TO PARSE")
    
# Wrapper that will call bundled tasks / parse calls
async def inventory_scrape_wrapper(char_names):
    # Need to pass in char_names
    semaphore = asyncio.Semaphore(8)
    async def limited_task(char_name):
        async with semaphore:
            return await inventory_scrape(char_name)
        
    tasks = [limited_task(char_name) for char_name in char_names]
    results = await asyncio.gather(*tasks)
    for result in results:
        if result:
            print(result)
    