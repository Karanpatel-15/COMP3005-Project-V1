import json
import psycopg2
import os
import time

# Database connection parameters
db_params = {
    'dbname': 'postgres',
    'user': 'postgres',
    'password': 'admin',
    'host': 'localhost',
    'port': 5432
}

types = {}

def insert_or_ignore(cursor, table, columns, values):
    """
    Insert a row into the table if it doesn't already exist.
    """
    query = f"INSERT INTO {table} ({', '.join(columns)}) VALUES ({', '.join(['%s' for _ in values])}) ON CONFLICT DO NOTHING"
    cursor.execute(query, values)

def insert_data(match_id, data):

    # Connect to the PostgreSQL database
    # conn = psycopg2.connect(**db_params)
    # cursor = conn.cursor()

    for match in data:
        # print type of event
        # types.add(match['type']['name'], match['type']['id'])
        if match['type']['name'] not in types:
            types[match['type']['name']] = match['type']['id']


    # Commit changes and close connection
    # conn.commit()
    # conn.close()

if __name__ == '__main__':
    start = time.time()
    for file in os.listdir("data/events"):
        if file.endswith(".json"):
            with open(os.path.join("data/events", file)) as f:
                data = json.load(f)
                print(f"Inserting data from {file}...")
                insert_data(file.split('.')[0], data)
    print(f"Time taken for events: {time.time() - start:.2f} seconds")
    for key in types:
        print(key, types[key])
