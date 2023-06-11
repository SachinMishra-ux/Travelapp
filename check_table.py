import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('travellers.db')

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Execute the SELECT query to retrieve table information
select_query = "SELECT * FROM travellers_data"
cursor.execute(select_query)

# Fetch all rows from the result set
rows = cursor.fetchall()

# Print the table structure
columns = [description[0] for description in cursor.description]
print("Table Structure:")
print(columns)

# Print the table content
print("Table Content:")
for row in rows:
    print(row)

# Close the connection
conn.close()
