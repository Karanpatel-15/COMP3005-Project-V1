import psycopg
import os
import csv

db_params = {
    'dbname': 'postgres',
    'user': 'postgres',
    'password': 'admin',
    'host': 'localhost',
    'port': 5432
}
conn = psycopg.connect(**db_params)
cursor = conn.cursor()

# In the La Liga season of 2020/2021, sort the players from highest to lowest based on their average
# xG scores. Output both the player names and their average xG scores. Consider only the players
# who made at least one shot (the xG scores are greater than 0).
def q_1():
    # TODO: FETCH THE SEASON ID
    seasonId = 4
    query = """
      SELECT player_name, AVG(event_statsbomb_xg)
      FROM season_event_mapping AS SEM
      JOIN event_shot ON SEM.event_id = event_shot.event_id
      JOIN player ON player.player_id = event_shot.event_player_id
      WHERE SEM.season_id = %s and event_shot.event_statsbomb_xg > 0
      GROUP BY player_name
      """
    cursor.execute(query, (seasonId,))
    results = cursor.fetchall()
    resultsInCSV = []
    with open('data/correct_csv/Q1.csv', mode='r', encoding='utf-8-sig') as file:
        # Creating a CSV DictReader object
        csv_reader = csv.DictReader(file)
        for row in resultsInCSV:
            resultsInCSV.append(row)
    print(resultsInCSV)


    return results
# In the La Liga season of 2020/2021, find the players with the most shots. Sort them from highest to
# lowest. Output both the player names and the number of shots. Consider only the players who
# made at least one shot (the lowest number of shots should be 1, not 0).
def q_2():
    seasonId = 4
    query = """
    SELECT player_name, COUNT(SEM.event_id)
      FROM season_event_mapping AS SEM
      JOIN event_shot ON SEM.event_id = event_shot.event_id
      JOIN player ON player.player_id = event_shot.event_player_id
      WHERE SEM.season_id = %s and event_shot.event_statsbomb_xg > 0
      GROUP BY player_name
          """
    cursor.execute(query, (seasonId,))
    results = cursor.fetchall()

# In the La Liga seasons of 2020/2021, 2019/2020, and 2018/2019 combined, find the players with the
# most first-time shots. Sort them from highest to lowest. Output the player names and the number
# of first time shots. Consider only the players who made at least one shot (the lowest number of shots
# should be 1, not 0).
def q_3():
    seasonIds = [4, 90, 42]
    query = """
    SELECT 
        p.player_name, 
        COUNT(es.event_id) AS first_time_shots
    FROM season_event_mapping AS sem
    JOIN event_shot AS es ON sem.event_id = es.event_id
    JOIN player AS p ON p.player_id = es.event_player_id
    WHERE sem.season_id IN (%s,%s,%s) AND es.event_first_time = true
    GROUP BY p.player_name
    HAVING COUNT(es.event_id) >= 1
    ORDER BY first_time_shots DESC;
          """
    cursor.execute(query, seasonIds)
    results = cursor.fetchall()
    print(results)

if __name__ == '__main__':
    q_1()