import psycopg

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
    print(results)
    return results

if __name__ == '__main__':
    q_1()