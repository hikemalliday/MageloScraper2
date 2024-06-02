# RoTPVP magelo scrape
Scrapes all public facing character inventories, outputs SQLite file. Now optimized with asyncio for fast runtime. Now takes about 15 minutes to complete.

Design:

1. Scrape all char names
2. Iterate over magelo using charnames as URLs
3. Use BeautifulSoup to parse HTML into python
4. Insert data into SQLite database

AsyncIO increased scrape speed by about 8x.
