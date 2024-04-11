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

seasonIds = {
    '2020/2021': 90,
    '2019/2020': 42,
    '2018/2019': 4,
    '2003/2004': 44
}
competitionIds = {
    'La Liga': 11,
    'Premier League': 2
}

# In the La Liga season of 2020/2021, sort the players from highest to lowest based on their average
# xG scores. Output both the player names and their average xG scores. Consider only the players
# who made at least one shot (the xG scores are greater than 0).
def q_1():
    # TODO: FETCH THE SEASON ID
    query = """
      SELECT player_name, AVG(event_statsbomb_xg) as avg_xg
      FROM competition_season_event_mapping AS SEM
      JOIN event_shot ON SEM.event_id = event_shot.event_id
      JOIN player ON player.player_id = event_shot.event_player_id
      WHERE SEM.season_id = %s and SEM.competition_id = %s and event_shot.event_statsbomb_xg > 0
      GROUP BY player_name
      ORDER BY avg_xg DESC

      """
    cursor.execute(query, (seasonIds['2020/2021'],competitionIds['La Liga']))
    results = cursor.fetchall()
    print(results)


    return results
# In the La Liga season of 2020/2021, find the players with the most shots. Sort them from highest to
# lowest. Output both the player names and the number of shots. Consider only the players who
# made at least one shot (the lowest number of shots should be 1, not 0).
def q_2():
    query = """
    SELECT player_name, COUNT(SEM.event_id) as number_shots
      FROM competition_season_event_mapping AS SEM
      JOIN event_shot ON SEM.event_id = event_shot.event_id
      JOIN player ON player.player_id = event_shot.event_player_id
      WHERE SEM.season_id = %s and SEM.competition_id = %s and event_shot.event_statsbomb_xg > 0
      GROUP BY player_name
      ORDER BY number_shots DESC
          """
    cursor.execute(query, (seasonIds['2020/2021'],competitionIds['La Liga']))
    results = cursor.fetchall()
    print(results)
    print(len(results))
    return  results
# In the La Liga seasons of 2020/2021, 2019/2020, and 2018/2019 combined, find the players with the
# most first-time shots. Sort them from highest to lowest. Output the player names and the number
# of first time shots. Consider only the players who made at least one shot (the lowest number of shots
# should be 1, not 0).
def q_3():
    query = """
    SELECT 
        p.player_name, 
        COUNT(es.event_id) AS first_time_shots
    FROM competition_season_event_mapping AS sem
    JOIN event_shot AS es ON sem.event_id = es.event_id
    JOIN player AS p ON p.player_id = es.event_player_id
    WHERE sem.season_id IN (%s,%s,%s) and sem.competition_id=%s 
    and es.event_first_time = true
    GROUP BY p.player_name
    HAVING COUNT(es.event_id) >= 1
    ORDER BY first_time_shots DESC;
          """
    cursor.execute(query, (seasonIds['2020/2021'],seasonIds['2019/2020'],seasonIds['2018/2019'], competitionIds['La Liga']))
    results = cursor.fetchall()
    return  results

# In the La Liga season of 2020/2021, find the teams with the most passes made. Sort them from
# highest to lowest. Output the team names and the number of passes. Consider the teams that
# make at least one pass (the lowest number of passes is 1, not 0).
def q_4():
    query = """
            Select team.team_name, COUNT(team.team_id) as number_of_passes from competition_season_event_mapping AS SEM 
        JOIN event_pass as EP on sem.event_id = EP.event_id
        JOIN player AS P ON P.player_id = EP.event_player
        JOIN lineup on lineup.player_id = P.player_id
        JOIN team on lineup.team_id = team.team_id
        WHERE SEM.season_id = %s and sem.competition_id=%s
        GROUP BY (team.team_id)
        ORDER BY number_of_passes DESC
    """
    cursor.execute(query, (seasonIds['2020/2021'],competitionIds['La Liga']))
    results = cursor.fetchall()
    return  results

# Q 5: In the Premier League season of 2003/2004, find the players who were the most intended recipients
# of passes. Sort them from highest to lowest. Output the player names and the number of times
# they were the intended recipients of passes. Consider the players who received at least one pass
# (the lowest number of times they were the intended recipients is 1, not 0).
def q_5():

    query = """
      Select P.player_name,  COUNT(EP.event_recipient_id) as count_intended_recipient from competition_season_event_mapping AS SEM 
    JOIN event_pass as EP on sem.event_id = EP.event_id
    JOIN player AS P ON P.player_id = EP.event_recipient_id
    WHERE SEM.season_id =%s and sem.competition_id=%s
	GROUP BY(P.player_name)  
    ORDER BY count_intended_recipient DESC
    """
    cursor.execute(query, (seasonIds['2003/2004'],competitionIds['Premier League']))
    results = cursor.fetchall()
    return  results

# In the Premier League season of 2003/2004, find the teams with the most shots made. Sort them
# from highest to lowest. Output the team names and the number of shots. Consider the teams that
# made at least one shot (the lowest number of shots is 1, not 0).
def q_6():

    query = """
        Select team.team_name, COUNT(team.team_id) as number_shots 
        from competition_season_event_mapping AS SEM 
        JOIN event_shot as ES on sem.event_id = ES.event_id
        JOIN player AS P ON P.player_id = ES.event_player_id
        JOIN lineup on lineup.player_id = P.player_id
        JOIN team on team.team_id = lineup.team_id
        WHERE SEM.season_id = %s and sem.competition_id=%s
        GROUP BY(team.team_name)
        ORDER BY number_shots DESC
    """
    cursor.execute(query, (seasonIds['2003/2004'],competitionIds['Premier League']))
    results = cursor.fetchall()
    return  results


# Q 7: In the La Liga season of 2020/2021, find the players who made the most through balls. Sort them
# from highest to lowest. Output the player names and the number of through balls. Consider the
# players who made at least one through ball pass (the lowest number of through balls is 1, not 0).
def q_7():
    print('----q7-----')

def runAll():
    q_1()
    q_2()
    q_3()
    q_4()
    q_5()
    q_6()

if __name__ == '__main__':
    runAll()
