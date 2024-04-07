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
    # csvResults = []
    # compare with values in csv
    # with open("./data/correct_csv/Q1.csv", mode='r', encoding='utf-8-sig') as file:
    #     # Creating a CSV DictReader object
    #     csv_reader = csv.DictReader(file)
    #     first_row = next(csv_reader)
    #     for row in csv_reader:
    #             csvResults.append(row)
    # for i in range(len(results)):
    #     resultInCsv = next((x for x in csvResults if x['PLAYER_NAME'] == results[i][0]), None)
    #     if resultInCsv is None:
    #         print(results[i], "Not found in csv")
    return results

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

if __name__ == '__main__':
    q_1()