import json
import psycopg
import os
import time

# Database connection parameters
db_params = {
    'dbname': 'postgres',
    'user': 'postgres',
    'password': '1234',
    'host': 'localhost',
    'port': 5432
}

def insert_or_ignore(cursor, table, columns, values):
    """
    Insert a row into the table if it doesn't already exist.
    """
    query = f"INSERT INTO {table} ({', '.join(columns)}) VALUES ({', '.join(['%s' for _ in values])}) ON CONFLICT DO NOTHING"
    cursor.execute(query, values)

def insert_competition_data(data):

    start = time.time()

    # Connect to the PostgreSQL database
    conn = psycopg.connect(**db_params)
    cursor = conn.cursor()

    # Iterate through JSON data and insert into tables
    for competition in data:

        # Insert competition data
        competition_id = competition['competition_id']
        country_name = competition['country_name']
        competition_name = competition['competition_name']
        competition_gender = competition['competition_gender']
        competition_youth = competition['competition_youth']
        competition_international = competition['competition_international']

        season_id = competition['season_id']
        season_name = competition['season_name']

        # Insert competition
        insert_or_ignore(cursor, 'competition', ['competition_id', 'country_name', 'competition_name', 'competition_gender', 'competition_youth', 'competition_international'], (competition_id, country_name, competition_name, competition_gender, competition_youth, competition_international))

        # Insert season
        insert_or_ignore(cursor, 'season', ['season_id', 'season_name'], (season_id, season_name))

        # Insert competition_season
        insert_or_ignore(cursor, 'competition_season', ['competition_id', 'season_id'], (competition_id, season_id))

    # Commit changes
    conn.commit()
    # Close connection
    conn.close()

    end = time.time()
    print(f"Time taken for competition: {end - start:.2f} seconds")

if __name__ == '__main__':
    with open(os.path.join("data", "competitions.json")) as f:
        data = json.load(f)
        insert_competition_data(data)