from datetime import datetime, timedelta
import os
import glob
import shutil

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

def is_dst(dt, year):
    # DST starts at 2 AM on the second Sunday in March
    dst_start = datetime(year, 3, 14 - (datetime(year, 3, 1).weekday() + 1), 2) - timedelta(days=7)
    # DST ends at 2 AM on the first Sunday in November
    dst_end = datetime(year, 11, 7 - datetime(year, 11, 1).weekday(), 2)
    return dst_start <= dt.replace(tzinfo=None) < dst_end

def date_time_string():
    now_utc = datetime.utcnow()
    houston_offset = -6
    if is_dst(now_utc, now_utc.year):
        houston_offset = -5  # Adjust for daylight saving time

    houston_time = now_utc + timedelta(hours=houston_offset)
    display_string = houston_time.strftime("%m/%d/%y %H:%M")
    file_string = display_string.replace("/", "-").replace(":", "-")
    
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
        item_name = 'Shimmering Pearl (EoV)'
    if item_id == '28054':
        item_name = 'Shimmering Pearl (Ragefire)'
    if item_id == '28047':
        item_name = 'Ornate Sea Shell (#1)'
    if item_id == '20856':
        item_name = 'Ornate Sea Shell (#2)'
    if item_name != '':
        return item_name
    
def delete_oldest_db_file():
    db_files = glob.glob(os.path.join('./data/', '*.db'))
    
    if len(db_files) <= 1:
        return

    oldest_file = min(db_files, key=os.path.getmtime)
    print(f"Deleting the oldest file: {oldest_file}")
    os.remove(oldest_file)

def copy_db_file():
    source_path = './data/inprogress/master.db'
    destination_dir = './data'
    new_filename = date_time_string() + '.db'
    destination_path = os.path.join(destination_dir, new_filename)
    shutil.copy2(source_path, destination_path)


