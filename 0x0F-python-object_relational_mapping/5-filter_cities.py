#!/usr/bin/python3
""" A module to select states """
if __name__ == "__main__":
    import MySQLdb
    import sys
    conn = MySQLdb.connect(host="localhost",
                           port=3306, user=sys.argv[1],
                           passwd=sys.argv[2],
                           db=sys.argv[3],
                           charset="utf8")
    cur = conn.cursor()
    cur.execute("""SELECT City FROM (
        SELECT cities.id AS ID, cities.name AS City,
        states.name AS State FROM cities
        JOIN states
        ON cities.state_id = states.id
        ORDER BY cities.id ASC) as Table1
        WHERE State=%s;
        """, (sys.argv[4],))
    query_rows = cur.fetchall()
    if query_rows:
        for row in query_rows:
            if row != query_rows[-1]:
                print("{}, ".format(*row), end="")
            else:
                print(*row)
    else:
        print()
    cur.close()
    conn.close()
