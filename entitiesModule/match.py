import psycopg
db_params = {
    'dbname': 'postgres',
    'user': 'postgres',
    'password': 'admin',
    'host': 'localhost',
    'port': 5432
}

def loadCompetitionMatches(competitionId, seasonId, cursor):
    query = "select match_id from match where season_id = %s and competition_id = %s"
    cursor.execute(query, (seasonId, competitionId))
    matchIdList = list()
    for row in cursor.fetchall():
        matchIdList.append(int(row[0]))
    return matchIdList
def getRequriedMatchIds():
    conn = psycopg.connect(**db_params)
    cursor = conn.cursor()
    competitionSeasonsToLoad = [(11, 4)]
    matchIds = []
    for data in competitionSeasonsToLoad:
        matchIds= matchIds + loadCompetitionMatches(data[0], data[1], cursor)
    conn.commit()
    conn.close()
    return list(matchIds)

