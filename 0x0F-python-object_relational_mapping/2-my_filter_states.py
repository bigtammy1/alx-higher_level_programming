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
    cur.execute("SELECT * FROM states WHERE name='{}' \
            ORDER BY id ASC".format(sys.argv[4]))
    query_rows = cur.fetchall()
    for row in query_rows:
        if row[1] == sys.argv[4]:
            print(row)
    cur.close()
    conn.close()
