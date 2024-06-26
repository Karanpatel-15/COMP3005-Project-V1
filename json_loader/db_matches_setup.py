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
    

def insert_manager(cursor, manager):
    """
    Insert manager data into the 'manager' table.
    """
    manager_data = (
        manager['id'],
        manager['name'],
        manager['nickname'],
        manager['dob'],
        manager['country']['name']
    )
    insert_or_ignore(cursor, 'manager', ['manager_id', 'manager_name', 'manager_nickname', 'manager_dob', 'country_name'], manager_data)

def insert_team_manager(cursor, team_id, manager_id):
    """
    Insert team-manager relationship data into the 'team_manager' table.
    """
    team_manager_data = (team_id, manager_id)
    insert_or_ignore(cursor, 'team_manager', ['team_id', 'manager_id'], team_manager_data)

def insert_match_data(cursor, competition_id, season_id, data):

    
    
    # Iterate through JSON data and insert into tables
    for match in data:

        # Insert competition data
        competition_name = match.get('competition', {}).get('competition_name', None)
        competition_country = match.get('competition', {}).get('country', {}).get('name', None)
        insert_or_ignore(cursor, 'competition', ['competition_id', 'country_name', 'competition_name'], (competition_id, competition_country, competition_name))

        season_name = match.get('season', {}).get('season_name', None)
        insert_or_ignore(cursor, 'season', ['season_id', 'season_name'], (season_id, season_name))

        # Insert home team data
        home_team_data = (
            match['home_team']['home_team_id'],
            match['home_team']['home_team_name'],
            match['home_team']['home_team_gender'],
            match['home_team']['country']['name']
        )
        insert_or_ignore(cursor, 'team', ['team_id', 'team_name', 'team_gender', 'country_name'], home_team_data)

        # Insert away team data
        away_team_data = (
            match['away_team']['away_team_id'],
            match['away_team']['away_team_name'],
            match['away_team']['away_team_gender'],
            match['away_team']['country']['name']
        )
        insert_or_ignore(cursor, 'team', ['team_id', 'team_name', 'team_gender', 'country_name'], away_team_data)


        # Insert stadium data
        if 'stadium' in match:
            stadium_data = (
                match['stadium']['id'],
                match['stadium']['name'],
                match['stadium']['country']['name']
            )
            insert_or_ignore(cursor, 'stadium', ['stadium_id', 'stadium_name', 'country_name'], stadium_data)

        # Insert referee data
        if 'referee' in match and match['referee'] is not None:
            referee_data = (
                match['referee']['id'],
                match['referee']['name'],
                match['referee']['country']['name']
            )
            insert_or_ignore(cursor, 'referee', ['referee_id', 'referee_name', 'country_name'], referee_data)
        
        home_team_data = (
            match['home_team']['home_team_id'],
            match['home_team']['home_team_name'],
            match['home_team']['home_team_gender'],
            match['home_team']['country']['name']
        )

        away_team_data = (
            match['away_team']['away_team_id'],
            match['away_team']['away_team_name'],
            match['away_team']['away_team_gender'],
            match['away_team']['country']['name']
        )

        # Insert team data
        insert_or_ignore(cursor, 'team', ['team_id', 'team_name', 'team_gender', 'country_name'], home_team_data)
        insert_or_ignore(cursor, 'team', ['team_id', 'team_name', 'team_gender', 'country_name'], away_team_data)

        # Insert manager data for home team
        if 'managers' in match['home_team']:
            for manager in match['home_team']['managers']:
                insert_manager(cursor, manager)
                insert_or_ignore(cursor, 'team_manager', ['team_id', 'manager_id'], (match['home_team']['home_team_id'], manager['id']))


        # Insert manager data for away team
        if 'managers' in match['away_team']:
            for manager in match['away_team']['managers']:
                insert_manager(cursor, manager)
                insert_or_ignore(cursor, 'team_manager', ['team_id', 'manager_id'], (match['away_team']['away_team_id'], manager['id']))

        # Insert match data
        match_data = (
            match['match_id'],
            match['season']['season_id'],
            match['competition']['competition_id'],
            match['match_date'] if 'match_date' in match else None,
            match['kick_off'] if 'kick_off' in match else None,
            match['stadium']['id'] if 'stadium' in match else None,
            match['referee']['id'] if 'referee' in match and match['referee'] is not None else None,
            match['home_team']['home_team_id'],
            match['away_team']['away_team_id'],
            match['home_score'],
            match['away_score'],
            match['match_status'] if 'match_status' in match else None,
            match['match_week'] if 'match_week' in match else None,
            match['competition_stage']['name'] if 'competition_stage' in match else None
        )
        insert_or_ignore(cursor, 'match', ['match_id','season_id', 'competition_id', 'match_date', 'kick_off', 'stadium_id', 'referee_id', 'home_team_id', 'away_team_id', 'home_score', 'away_score', 'match_status', 'match_week', 'competition_stage'], match_data)

        # Insert competition_season
        insert_or_ignore(cursor, 'competition_season', ['competition_id', 'season_id'], (competition_id, season_id))
        
        # Insert season_match
        # insert_or_ignore(cursor, 'season_match', ['season_id', 'match_id'], (season_id, match['match_id']))
    

if __name__ == '__main__':
    start = time.time()

    # Connect to the PostgreSQL database
    conn = psycopg.connect(**db_params)
    cursor = conn.cursor()

    COMPETITION_SEASONS_TO_LOAD = [(11,4), (11,42), (11,90), (2,44)]
    competition_season_map = {}
    for competition_id, season_id in COMPETITION_SEASONS_TO_LOAD:
        if competition_id in competition_season_map:
            competition_season_map[competition_id].append(season_id)
        else:
            competition_season_map[competition_id] = [season_id]

    print(competition_season_map)

    matchFolder = os.path.join("data","matches")
    for dir in os.listdir(matchFolder):
        if not os.path.isdir(os.path.join(matchFolder, dir)) or int(dir) not in competition_season_map:
            continue
        competition_id = int(dir)
        for file in os.listdir(os.path.join(matchFolder, dir)):
            match_id = int(file.split('.')[0])  
            requiredSeason = set(competition_season_map[competition_id])
            if match_id in requiredSeason:
                with open(os.path.join(matchFolder, dir, file)) as f:
                    data = json.load(f)
                    print(f"Inserting match data from competition {competition_id} and season {file}...")
                    insert_match_data(cursor, dir,file.split('.')[0], data)
    
    # Commit changes and close connection
    conn.commit()
    conn.close()
    print(f"Time taken: {time.time()-start} seconds")