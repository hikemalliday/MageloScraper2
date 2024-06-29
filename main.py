from char_name_scrape import char_name_scrape
import asyncio
from config import DATE_TIME
from helper import date_time_string, delete_oldest_db_file, copy_db_file
from table import create_tables, delete_tables
from inventory_scrape import inventory_scrape_wrapper
import time


def main():
    delete_tables()
    create_tables()
    char_names = char_name_scrape()
    asyncio.run(inventory_scrape_wrapper(char_names))
    copy_db_file()
    delete_oldest_db_file()

if __name__ == "__main__":
    #DATE_TIME["date_time"] = "./data/" + date_time_string() + ".db"
    main()
    
    # Run once an hour
    while True:
        time.sleep(3600)
        main()
