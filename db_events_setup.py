import json
import psycopg
import os
import time
from entitiesModule.match import getRequriedMatchIds
from concurrent.futures import ThreadPoolExecutor
from eventStratigiesModule import EventStrategyManager
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

def handle_half_start(cursor, event_id, event):
    event_duration = event.get('duration', None)
    insert_or_ignore(cursor, 'event_half_start', ['event_id', 'event_duration'], [event_id, event_duration])

def handle_half_end(cursor, event_id, event):
    event_duration = event.get('duration', None)
    insert_or_ignore(cursor, 'event_half_end', ['event_id', 'event_duration'], [event_id, event_duration])

def insert_data(cursor, season_id,competition_id, match_id, data):

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
        insert_or_ignore(cursor, 'competition_season_event_mapping', ['season_id', 'competition_id', 'event_id'], [season_id, competition_id, event_id])
        eventStratigieManager = EventStrategyManager.EventStrategyManager()
        #switch case for different event types
        strategy = eventStratigieManager.get_strategy_by_id(event_typeId)
        if strategy is not None:
            strategy.handle(cursor, event)
        else:
            continue



def loadCompetitionMatches( competitionId, seasonId, cursor):
    query = "select match_id from match where season_id = %s and competition_id = %s"
    cursor.execute(query, (seasonId, competitionId))
    matchIdList = set()
    for row in cursor.fetchall():
        matchIdList.add(row[0])

def loadMatchMetadataMapping(matchIdsArray, cursor):
    matchIdToMetadata = {}
    placeholders = ', '.join(['%s'] * len(matchIdsArray))
    query = "SELECT match_id, season_id, competition_id FROM match WHERE match_id IN ({})".format(placeholders)
    cursor.execute(query, matchIdsArray)
    for row in cursor.fetchall():
        matchIdToMetadata[row[0]] = {
            'season_id': row[1],
            'competition_id': row[2]
        }
    return matchIdToMetadata

if __name__ == '__main__':
    start = time.time()
    
    matchesToSeasonMapping = {}

    # Connect to the PostgreSQL database
    conn = psycopg.connect(**db_params)
    cursor = conn.cursor()
    counter = 0

    matchesInQuery = getRequriedMatchIds()
    matchMetadataMapping = loadMatchMetadataMapping(matchesInQuery, cursor)
    eventFolder = os.environ.get("EVENT_FOLDER_PATH", os.path.join("data","events"))

    for file in os.listdir(eventFolder):
        matchId = int(file.split('.')[0])
        if matchId in matchesInQuery:
            with open(os.path.join(eventFolder, file)) as f:
                data = json.load(f)
                matchId = int(file.split('.')[0])
                metadata = matchMetadataMapping.get(matchId, None)
                season_id = metadata['season_id']
                competition_id = metadata['competition_id']
                insert_data(cursor, season_id, competition_id, matchId, data)
        counter += 1
        print(f"Inserted event data for {counter} matches")

    conn.commit()
    conn.close()
    print(f"Time taken for events: {time.time() - start:.2f} seconds")
