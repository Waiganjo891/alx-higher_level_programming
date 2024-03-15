#!/usr/bin/python3
"""  lists all states from the database hbtn_0e_0_usa """
import MySQLdb
import sys


def list_states_starting_with_N(user, password, db_name):
    conn = MySQLdb.connect(
        host='localhost', user=user, passwd=password, db=db_name
    )
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id, name FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
    )
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    conn.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(
            "Usage: python script.py <mysql_username> <mysql_password> "
            "<database_name>"
        )
        sys.exit(1)
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    list_states_starting_with_N(user, password, db_name)
