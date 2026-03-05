#!/usr/bin/python3
"""
This script lists all states from the database hbtn_0e_0_usa.
It takes 3 arguments: mysql username, mysql password and database name.
"""
import MySQLdb
import sys


def main():
    """
    Connects to the database and retrieves all states
    sorted by id in ascending order.
    """
    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    # Create a cursor object
    cursor = db.cursor()

    # Execute the SQL query
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all the rows
    query_rows = cursor.fetchall()

    # Display results
    for row in query_rows:
        print(row)

    # Close cursor and database connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
