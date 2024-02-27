import sqlite3

def create_db():
    with open('learning.sql', 'r') as file:
        sql = file.read()
    
    with sqlite3.connect('learning.db') as con:
        cur = con.cursor()
        cur.executescript(sql)

if __name__ == '__main__':
    create_db()