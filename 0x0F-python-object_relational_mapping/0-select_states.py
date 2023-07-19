#!/usr/bin/python3

"""Script to list all states in the database hbtn_0e_0_usa."""


import MySQLdb
import sys


if __name__ == "__main__":
    argv = sys.argv[1:]
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[0], passwd=argv[1], db=argv[2])
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    result = cur.fetchall()
    for r in result:
        print(r)
    cur.close()
    conn.close()
