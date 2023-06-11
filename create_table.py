import sqlite3

# Connect to the database (or create if it doesn't exist)
conn = sqlite3.connect('travellers.db')

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Create a table
create_table_query = '''
CREATE TABLE IF NOT EXISTS travellers_data (
    id INTEGER PRIMARY KEY,
    date DATE,
    number_of_travellers INTEGER
)
'''
cursor.execute(create_table_query)

# Commit the changes and close the connection
conn.commit()
conn.close()

