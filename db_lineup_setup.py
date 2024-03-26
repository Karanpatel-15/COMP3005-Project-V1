import json
import psycopg2
import os

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


def insert_data(data):

    # Connect to the PostgreSQL database
    conn = psycopg2.connect(**db_params)
    cursor = conn.cursor()

    # Iterate through JSON data and insert into tables
    for team_data in data:
        # Insert team data
        team_id = team_data['team_id']
        team_name = team_data['team_name']
        
        # Insert team
        insert_or_ignore(cursor, 'team', ['team_id', 'team_name'], (team_id, team_name), 'team_id')

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

            # Insert positions
            positions = player_data.get('positions', [])
            for position_data in positions:
                position_id = position_data['position_id']
                position = position_data['position']
                from_time = position_data['from']
                to_time = position_data['to']
                from_period = position_data['from_period']
                to_period = position_data['to_period']
                start_reason = position_data['start_reason']
                end_reason = position_data['end_reason']

                insert_or_ignore(cursor, 'position', ['position_id', 'position', 'from_time', 'to_time', 'from_period', 'to_period', 'start_reason', 'end_reason'], 
                                  (position_id, position, from_time, to_time, from_period, to_period, start_reason, end_reason))

                # Insert lineup entry
                insert_or_ignore(cursor, 'lineup', ['player_id', 'position_id'], (player_id, position_id))
        
            # Insert cards
            cards = player_data.get('cards', [])
            for card_data in cards:
                card_time = card_data['time']
                card_type = card_data['card_type']
                card_reason = card_data['reason']
                card_period = card_data['period']

                insert_or_ignore(cursor, 'card', ['card_time', 'card_type', 'card_reason', 'card_period'], (card_time, card_type, card_reason, card_period))

                # Get card_id for lineup entry
                cursor.execute("SELECT card_id FROM card WHERE card_time = %s AND card_type = %s AND card_reason = %s AND card_period = %s", (card_time, card_type, card_reason, card_period))
                card_id = cursor.fetchone()[0]

                # Update lineup entry with card_id
                cursor.execute("UPDATE lineup SET card_id = %s WHERE player_id = %s", (card_id, player_id))

    # Commit changes and close connection
    conn.commit()
    conn.close()

if __name__ == '__main__':
    for file in os.listdir("data/lineups"):
        if file.endswith(".json"):
            with open(os.path.join("data/lineups", file)) as f:
                data = json.load(f)
                print(f"Inserting data from {file}...")
                insert_data(data)
