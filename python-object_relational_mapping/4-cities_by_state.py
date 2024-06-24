#!/usr/bin/env python3
import MySQLdb
import sys

if __name__ == "__main__":
    # Get MySQL username, password, and database name from arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Connect to the MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=mysql_username, passwd=mysql_password, db=database_name)

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute the SQL query to find all cities with their states
    query = """
    SELECT cities.id, cities.name, states.name 
    FROM cities 
    JOIN states ON cities.state_id = states.id 
    ORDER BY cities.id ASC
    """
    cursor.execute(query)

    # Fetch all the rows returned by the query
    cities = cursor.fetchall()

    # Print the results
    for city in cities:
        print(city)

    # Close the cursor and the database connection
    cursor.close()
    db.close()
