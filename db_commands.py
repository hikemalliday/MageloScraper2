import sqlite3
from config import DATE_TIME

# NOTE: For bulk inserts
def insert_char_inventories(rows: list):
    try:
        conn = sqlite3.connect('./data/master.db')
        cursor = conn.cursor()

        query = '''INSERT INTO char_inventory (
            char_name,
            item_name,
            item_count,
            item_location,
            char_guild
        ) VALUES (?, ?, ?, ?, ?)
    '''
        cursor.executemany(query, rows)
        conn.commit()
    except Exception as e:
        print(e)
        return str(e)
    
    finally:
        conn.close()

def insert_char_names(char_names: list):
    try:
        conn = sqlite3.connect('./data/master.db')
        cursor = conn.cursor()

        query = '''INSERT INTO char_names (
            char_name
        ) VALUES (?)
'''
        cursor.executemany(query, char_names)
        conn.commit()
    except Exception as e:
        print(e)
        return str(e)
    
    finally:
        conn.close()


        