import sqlite3

def create_table():
    con = sqlite3.connect('students.db') 
    con.execute(
        """
        CREATE TABLE IF NOT EXISTS contact(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT,
        email TEXT, 
        phone TEXT,
        message TEXT
        )
    """
    )

    con.close() 