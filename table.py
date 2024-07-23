import sqlite3
from config import DATE_TIME

def create_char_inventory_table():
    try:

        conn = sqlite3.connect('./data/inprogress/master.db')
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS char_inventory (
                id INTEGER PRIMARY KEY,
                char_name TEXT,
                char_guild TEXT DEFAULT '',
                item_name TEXT,
                item_count INTEGER DEFAULT 1,
                item_location TEXT
            )
        ''')
        conn.commit()
        return "char_inventory table created."
    except Exception as e:
        print(e)
        return str(e)
    finally:
        conn.close()

def create_char_names_table():
    try:
        conn = sqlite3.connect('./data/inprogress/master.db')
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS char_names (
                       id INTEGER PRIMARY KEY,
                       char_name TEXT
            )
''')
        conn.commit()
        return "char_names table created."
    except Exception as e:
        print(e)
        return str(e)
    finally:
        conn.close()

def delete_tables():
    try:
        conn = sqlite3.connect('./data/inprogress/master.db')
        cursor = conn.cursor()
        query = '''DELETE FROM char_names'''
        cursor.execute(query)
        query = '''DELETE FROM char_inventory'''
        cursor.execute(query)
        conn.commit()
    except Exception as e:
        print(e)
        return str(e)
    finally:
        if conn:
            conn.close()

def create_tables():
    create_char_inventory_table()
    create_char_names_table()