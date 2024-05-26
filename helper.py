from datetime import datetime
import os
import glob
import time

def extract_guild_name(tag):
    a_tags = tag.find_all("a")
    if a_tags:
        for a_tag in a_tags:
            href_value = a_tag.get('href', '')
            if href_value:
                # Split the href_value by '&'
                parameters = href_value.split('&')
                # Find the parameter containing the guild name
                for param in parameters:
                    if param.startswith('guild='):
                        # Extract the guild name from the parameter
                        guild_name = param.split('=')[1]
                        print("GUILD NAME FOUND:", guild_name)
                        return guild_name
    return ""

def date_time_string():
    current_datetime = datetime.now()
    # Create a string with colons for display
    display_string = current_datetime.strftime("%m/%d/%y %H/%M")
    # Replace colons and slashes with underscores or other valid characters for file name
    file_string = display_string.replace("/", "-")
    return file_string

def get_item_from_id(item_id) -> str:
    item_name = ''
    if item_id == '19956':
        item_name = 'Piece of a medallion (Pained Soul)'
    if item_id == '19957':
        item_name = 'Piece of a medallion (Rotting Skeleton)'
    if item_id == '19958':
        item_name = 'Piece of a medallion (Burnished Wooden Stave)'
    if item_id == '19959':
        item_name = 'Piece of a medallion (A Bloodgill Maurader)'
    if item_id == '19960':
        item_name = 'Piece of a medallion (An Ancient Jarsath)'
    if item_id == '19961':
        item_name = 'Piece of a medallion (Swamp of No Hope)'
    if item_id == '19962':
        item_name = 'Piece of a medallion (Kaesora)'
    if item_id == '19963':
        item_name = 'Piece of a medallion (Verix Kyloxs Remains)'
    if item_id == '19964':
        item_name = 'Piece of a medallion (Chardok)'
    if item_id == '20863':
        item_name = 'Shimmering Peal (EoV)'
    if item_id == '28054':
        item_name = 'Shimmering Pearl (Ragefire)'
    if item_id == '28047':
        item_name = 'Ornate Sea Shell (#1)'
    if item_id == '20856':
        item_name = 'Ornate Sea Shell (#2)'
    if item_name != '':
        return item_name
    
def delete_oldest_db_file():
    # Get a list of all .db files in the directory
    db_files = glob.glob(os.path.join('./data/', '*.db'))

    if not db_files:
        print("No .db files found in the directory.")
        return

    # Find the oldest .db file
    oldest_file = min(db_files, key=os.path.getmtime)

    # Print the file that will be deleted
    print(f"Deleting the oldest file: {oldest_file}")

    # Delete the oldest file
    os.remove(oldest_file)
