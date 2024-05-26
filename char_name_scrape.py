import requests
import omit

from bs4 import BeautifulSoup
from inventory_scrape import inventory_scrape

async def fetch(session, url, semaphore):
    async with semaphore:
        async with session.get(url, verify_ssl=True) as response:
            return await response.text()

def char_name_scrape() -> list:
    base_url = "https://rotpvp.com/magelo/"
    next_page = True
    found_next = False
    next_url = ''
    first_url = "https://rotpvp.com/magelo/index.php?page=search&name=&guild="
    response = None
    char_name_list = []
    while next_page:
        found_next = False
        if first_url:
            response = requests.get(first_url, verify=True)
            first_url = ''
        else:
            response = requests.get(next_url, verify=True)
        if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                char_names = soup.find_all('a')
                for char_name in char_names:
                    try:
                        # Filter away the numbers in the scrape
                        int(char_name.text)
                        continue
                    except:
                        if char_name.text == "Next":
                            next_url = base_url + char_name.get('href')
                            found_next = True
                            continue
                        if char_name.text in omit.char_name_scrape_omit:
                            continue
                        if char_name.text not in char_name_list:
                            char_name_list.append(char_name.text)
                        print(char_name.text)
                if found_next == False:
                    break
    return char_name_list

def inventory_scrape_wrapper(char_names):
    for char in char_names:
        inventory_scrape(char)
        


