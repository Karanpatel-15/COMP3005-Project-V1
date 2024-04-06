import json
import psycopg
import os
import time
from eventStratigiesModule import EventStrategyManager
# Database connection parameters
db_params = {
    'dbname': 'postgres',
    'user': 'postgres',
    'password': 'admin',
    'host': 'localhost',
    'port': 5432
}

RequiredSeasonId = {
    '2020/2021': 42,
    '2019/2020': 90,
    '2018/2019': 4,
    '2003/2004': 44 
}

def insert_or_ignore(cursor, table, columns, values):
    """
    Insert a row into the table if it doesn't already exist.
    """
    query = f"INSERT INTO {table} ({', '.join(columns)}) VALUES ({', '.join(['%s' for _ in values])}) ON CONFLICT DO NOTHING"
    cursor.execute(query, values)

def handle_half_start(cursor, event_id, event):
    event_duration = event.get('duration', None)
    insert_or_ignore(cursor, 'event_half_start', ['event_id', 'event_duration'], [event_id, event_duration])

def handle_half_end(cursor, event_id, event):
    event_duration = event.get('duration', None)
    insert_or_ignore(cursor, 'event_half_end', ['event_id', 'event_duration'], [event_id, event_duration])

def insert_data(season_id, match_id, data):

    # Connect to the PostgreSQL database
    conn = psycopg.connect(**db_params)
    cursor = conn.cursor()
    for event in data:
        event_id = event.get('id', None)
        event_index = event.get('index', None)
        event_period = event.get('period', None)
        event_timestamp = event.get('timestamp', None)
        event_minute = event.get('minute', None)
        event_second = event.get('second', None)
        event_type = event.get('type', None).get('name', None)
        event_typeId = event.get('type', None).get('id', None)
        event_possession = event.get('possession', None)
        event_possession_team_id = event.get('possession_team', None).get('id', None)
        event_play_pattern = event.get('play_pattern', None).get('name', None)
        event_team_id = event.get('team', None).get('id', None)

        # Insert event into the table
        insert_or_ignore(cursor, 'event', ['event_id', 'event_index', 'event_period', 'event_timestamp', 'event_minute', 'event_second', 'event_type', 'event_possession', 'event_possession_team_id', 'event_play_pattern', 'event_team_id'], [event_id, event_index, event_period, event_timestamp, event_minute, event_second, event_type, event_possession, event_possession_team_id, event_play_pattern, event_team_id])
        insert_or_ignore(cursor, 'match_event', ['match_id', 'event_id'], [match_id, event_id])
        insert_or_ignore(cursor, 'season_event_mapping', ['season_id', 'event_id'], [season_id, event_id])
        eventStratigieManager = EventStrategyManager.EventStrategyManager()
        #switch case for different event types
        strategy = eventStratigieManager.get_strategy_by_id(event_typeId)
        if strategy is not None:
            strategy.handle(cursor, event)
        else:
            continue


    # Commit changes and close connection
    conn.commit()
    conn.close()

if __name__ == '__main__':

    matchesToSeasonMapping = {}

    # Connect to the PostgreSQL database
    conn = psycopg.connect(**db_params)
    cursor = conn.cursor()

    query = "SELECT season_id, match_id from season_match WHERE season_id in (42, 90, 4, 44)"
    cursor.execute(query)
    
    for row in cursor.fetchall():
        season_id = row[0]
        match_id = row[1]
        matchesToSeasonMapping[match_id] = season_id

    conn.commit()
    conn.close() 

    print(matchesToSeasonMapping)

    start = time.time()
    for file in os.listdir(os.path.join("data","events")):
        if int(file.split('.')[0]) in matchesToSeasonMapping:
            with open(os.path.join("data","events", file)) as f:
                data = json.load(f)
                print(f"Inserting data from {file}...")
                matchId = file.split('.')[0]
                season_id = matchesToSeasonMapping[matchId]
                insert_data(season_id, matchId, data)
    print(f"Time taken for events: {time.time() - start:.2f} seconds")