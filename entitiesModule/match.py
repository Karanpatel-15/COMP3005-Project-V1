


def getMatchMetadataById(cursor, matchId):
    cursor.execute("SELECT * FROM match WHERE match_id = %s", (matchId))
    fetchedData = cursor.fetchone()
    data = {}
    data['match_id'] = fetchedData[0]
    data['match_data'] = fetchedData[1]
    data['kick_off'] = fetchedData[2]
    data['stadium_id'] = fetchedData[3]
    data['referee_id'] = fetchedData[4]
    data['home_team_id'] = fetchedData[5]
    data['away_team_id'] = fetchedData[6]
    data['home_score']= fetchedData[7]
    data['away_score'] = fetchedData[8]
    



def getMatchDataByMatch(cursor, matchId):
    cursor.execute("SELECT * FROM match WHERE match_id = %s", (matchId))
    return cursor.fetchone()[3]