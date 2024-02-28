import sqlite3


def query_1():
    with open("query_1.sql", "r") as file:
        sql = file.read()

    with sqlite3.connect("learning.db") as con:
        cur = con.cursor()
        cur.executescript(sql)
        return cur.fetchall()


if __name__ == "__main__":
    print(query_1())
