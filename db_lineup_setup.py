import json
import psycopg
import os
import time
from entitiesModule.match import getRequriedMatchIds

# Database connection parameters
db_params = {
    'dbname': 'postgres',
    'user': 'postgres',
    'password': 'admin',
    'host': 'localhost',
    'port': 5432
}

def insert_or_ignore(cursor, table, columns, values):
    """
    Insert a row into the table if it doesn't already exist.
    """
    query = f"INSERT INTO {table} ({', '.join(columns)}) VALUES ({', '.join(['%s' for _ in values])}) ON CONFLICT DO NOTHING"
    cursor.execute(query, values)

def insert_data(cursor, match_id, data):

    # Insert match
    insert_or_ignore(cursor, 'match', ['match_id'], (match_id,))

    # Iterate through JSON data and insert into tables
    for team_data in data:
        # Insert team data
        team_id = team_data['team_id']
        team_name = team_data['team_name']
        
        # Insert team
        insert_or_ignore(cursor, 'team', ['team_id', 'team_name'], (team_id, team_name))

        # Insert lineup data
        lineup = team_data.get('lineup', [])
        for player_data in lineup:
            player_id = player_data.get('player_id')
            player_name = player_data.get('player_name')
            player_nickname = player_data.get('player_nickname', None)
            jersey_number = player_data.get('jersey_number', None)
            country_name = player_data.get('country', {}).get('name', None)

            # Insert player
            insert_or_ignore(cursor, 'player', ['player_id', 'player_name', 'player_nickname', 'jersey_number', 'country_name'], (player_id, player_name, player_nickname, jersey_number, country_name))
            
            # Insert lineup relationship
            insert_or_ignore(cursor, 'lineup', ['match_id', 'team_id', 'player_id'], (match_id, team_id, player_id))

            # Insert positions
            positions = player_data.get('positions', [])
            for position_data in positions:
                position_id = position_data.get('position_id', None)
                position = position_data.get('position', None)
                from_time = position_data.get('from', None)
                to_time = position_data.get('to', None)
                from_period = position_data.get('from_period', None)
                to_period = position_data.get('to_period', None)
                start_reason = position_data.get('start_reason', None)
                end_reason = position_data.get('end_reason', None)

                insert_or_ignore(cursor, 'position', ['position_id', 'player_id', 'match_id', 'position', 'from_time', 'to_time', 'from_period', 'to_period', 'start_reason', 'end_reason'], 
                                  (position_id, player_id, match_id, position, from_time, to_time, from_period, to_period, start_reason, end_reason))
        
            # Insert cards
            cards = player_data.get('cards', [])
            for card_data in cards:
                card_time = card_data.get('time', None)
                card_type = card_data.get('card_type', None)
                card_reason = card_data.get('reason', None)
                card_period = card_data.get('period', None)

                insert_or_ignore(cursor, 'card', ['player_id', 'match_id', 'card_time', 'card_type', 'card_reason', 'card_period'], (player_id, match_id, card_time, card_type, card_reason, card_period))

if __name__ == '__main__':
    start = time.time()

    # Connect to the PostgreSQL database
    conn = psycopg.connect(**db_params)
    cursor = conn.cursor()
    
    requiredMatches = getRequriedMatchIds()

    lineupFolder = os.environ.get("LINEUP_FOLDER_PATH", os.path.join("data","lineups"))

    for file in os.listdir(lineupFolder):
        match_id = int(file.split('.')[0])
        if match_id in requiredMatches:
            with open(os.path.join(lineupFolder, file)) as f:
                print(f"Inserting lineup data for match {match_id}")
                data = json.load(f)
                insert_data(cursor, match_id, data)
    conn.commit()
    conn.close() 
    print(f"Time taken for lineup: {time.time() - start:.2f} seconds")
