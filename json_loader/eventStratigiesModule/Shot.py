
from db_events_setup import insert_or_ignore

id = 16

# CREATE TABLE IF NOT EXISTS event_shot (
#     id UUID,
#     player_id INTEGER,
#     position VARCHAR(100),
#     team_id INTEGER,
#     location_x FLOAT,
#     location_y FLOAT,
#     duration FLOAT,
#     out BOOLEAN,
#     under_pressure BOOLEAN,
#     off_camera BOOLEAN,
#     statsbomb_xg FLOAT,
#     end_location_x FLOAT,
#     end_location_y FLOAT,
#     body_part VARCHAR(100),
#     outcome VARCHAR(100),
#     first_time BOOLEAN,
#     technique VARCHAR(100),
#     deflected BOOLEAN,
#     one_on_one BOOLEAN,
#     aerial_won BOOLEAN,
#     saved_to_post BOOLEAN,
#     redirect BOOLEAN,
#     open_goal BOOLEAN,
#     follows_dribble BOOLEAN,
#     saved_off_target BOOLEAN,
#     freeze_frame_id INTEGER,
#     FOREIGN KEY (id) REFERENCES event(id),
#     FOREIGN KEY (player) REFERENCES player(player_id),
#     FOREIGN KEY (team_id) REFERENCES team(team_id),
#     FOREIGN KEY (freeze_frame_id) REFERENCES freeze_frame(freeze_frame_id),
#     UNIQUE (id)   
# );

# {
#   "id" : "37f411d5-c045-480a-a61a-07c75a099ee2",
#   "index" : 97,
#   "period" : 1,
#   "timestamp" : "00:01:46.003",
#   "minute" : 1,
#   "second" : 46,
#   "type" : {
#     "id" : 16,
#     "name" : "Shot"
#   },
#   "possession" : 8,
#   "possession_team" : {
#     "id" : 210,
#     "name" : "Real Sociedad"
#   },
#   "play_pattern" : {
#     "id" : 1,
#     "name" : "Regular Play"
#   },
#   "team" : {
#     "id" : 210,
#     "name" : "Real Sociedad"
#   },
#   "player" : {
#     "id" : 6721,
#     "name" : "Willian José da Silva"
#   },
#   "position" : {
#     "id" : 23,
#     "name" : "Center Forward"
#   },
#   "location" : [ 109.8, 40.0 ],
#   "duration" : 0.527253,
#   "related_events" : [ "53f45cc2-9e64-40be-8b81-e7c87a922359" ],
#   "shot" : {
#     "statsbomb_xg" : 0.087394096,
#     "end_location" : [ 117.7, 40.0, 0.9 ],
#     "key_pass_id" : "5bfc601b-0593-439c-95e3-d5b2efeab6d1",
#     "body_part" : {
#       "id" : 37,
#       "name" : "Head"
#     },
#     "type" : {
#       "id" : 87,
#       "name" : "Open Play"
#     },
#     "outcome" : {
#       "id" : 100,
#       "name" : "Saved"
#     },
#     "technique" : {
#       "id" : 93,
#       "name" : "Normal"
#     },
#     "freeze_frame" : [ {
#       "location" : [ 91.6, 59.6 ],
#       "player" : {
#         "id" : 3501,
#         "name" : "Philippe Coutinho Correia"
#       },
#       "position" : {
#         "id" : 21,
#         "name" : "Left Wing"
#       },
#       "teammate" : false
#     }, {
#       "location" : [ 86.1, 32.6 ],
#       "player" : {
#         "id" : 5477,
#         "name" : "Ousmane Dembélé"
#       },
#       "position" : {
#         "id" : 17,
#         "name" : "Right Wing"
#       },
#       "teammate" : false
#     }, {
#       "location" : [ 97.7, 54.8 ],
#       "player" : {
#         "id" : 5211,
#         "name" : "Jordi Alba Ramos"
#       },
#       "position" : {
#         "id" : 6,
#         "name" : "Left Back"
#       },
#       "teammate" : false
#     }, {
#       "location" : [ 108.6, 59.8 ],
#       "player" : {
#         "id" : 5203,
#         "name" : "Sergio Busquets i Burgos"
#       },
#       "position" : {
#         "id" : 10,
#         "name" : "Center Defensive Midfield"
#       },
#       "teammate" : false
#     }, {
#       "location" : [ 110.2, 57.1 ],
#       "player" : {
#         "id" : 5216,
#         "name" : "Andrés Iniesta Luján"
#       },
#       "position" : {
#         "id" : 15,
#         "name" : "Left Center Midfield"
#       },
#       "teammate" : false
#     }, {
#       "location" : [ 104.6, 43.4 ],
#       "player" : {
#         "id" : 5470,
#         "name" : "Ivan Rakitić"
#       },
#       "position" : {
#         "id" : 13,
#         "name" : "Right Center Midfield"
#       },
#       "teammate" : false
#     }, {
#       "location" : [ 109.7, 47.4 ],
#       "player" : {
#         "id" : 6196,
#         "name" : "Yerry Fernando Mina González"
#       },
#       "position" : {
#         "id" : 5,
#         "name" : "Left Center Back"
#       },
#       "teammate" : false
#     }, {
#       "location" : [ 111.8, 40.4 ],
#       "player" : {
#         "id" : 5213,
#         "name" : "Gerard Piqué Bernabéu"
#       },
#       "position" : {
#         "id" : 3,
#         "name" : "Right Center Back"
#       },
#       "teammate" : false
#     }, {
#       "location" : [ 110.9, 35.4 ],
#       "player" : {
#         "id" : 6374,
#         "name" : "Nélson Cabral Semedo"
#       },
#       "position" : {
#         "id" : 2,
#         "name" : "Right Back"
#       },
#       "teammate" : false
#     }, {
#       "location" : [ 118.0, 41.3 ],
#       "player" : {
#         "id" : 20055,
#         "name" : "Marc-André ter Stegen"
#       },
#       "position" : {
#         "id" : 1,
#         "name" : "Goalkeeper"
#       },
#       "teammate" : false
#     }, {
#       "location" : [ 84.0, 32.3 ],
#       "player" : {
#         "id" : 6674,
#         "name" : "Alberto De La Bella Madureño"
#       },
#       "position" : {
#         "id" : 6,
#         "name" : "Left Back"
#       },
#       "teammate" : true
#     }, {
#       "location" : [ 98.3, 50.8 ],
#       "player" : {
#         "id" : 6669,
#         "name" : "David Zurutuza Veillet"
#       },
#       "position" : {
#         "id" : 11,
#         "name" : "Left Defensive Midfield"
#       },
#       "teammate" : true
#     }, {
#       "location" : [ 110.3, 61.4 ],
#       "player" : {
#         "id" : 6330,
#         "name" : "Adnan Januzaj"
#       },
#       "position" : {
#         "id" : 12,
#         "name" : "Right Midfield"
#       },
#       "teammate" : true
#     }, {
#       "location" : [ 109.6, 45.9 ],
#       "player" : {
#         "id" : 6685,
#         "name" : "Mikel Oyarzabal Ugarte"
#       },
#       "position" : {
#         "id" : 16,
#         "name" : "Left Midfield"
#       },
#       "teammate" : true
#     }, {
#       "location" : [ 106.2, 33.0 ],
#       "player" : {
#         "id" : 6695,
#         "name" : "Juan Miguel Jiménez López"
#       },
#       "position" : {
#         "id" : 19,
#         "name" : "Center Attacking Midfield"
#       },
#       "teammate" : true
#     } ]
#   }
# }
class Strategy:
    def handle(self,cursor,payload):
        # print("Inserting Shot  " + str(payload))
        if (payload.get('shot', None) == None):
            # print("Shot is None")
            return

        event_id = payload.get('id', None)
        player_id = payload.get('player').get('id')
        event_player_name = payload.get('player').get('name')
        event_statsbomb_xg = payload.get('shot', None).get('statsbomb_xg')
        event_first_time = payload.get('shot', None).get('first_time')
        competition_id = payload.get('competition_id')
        season_id = payload.get('season_id')
        payload = {
            "event_id": event_id,
            "event_player_id": player_id,
            "event_player_name": event_player_name,
            "event_statsbomb_xg": event_statsbomb_xg,
            "event_first_time": event_first_time,
            "event_competition_id": competition_id,
            "event_season_id": season_id
        }
        cols = list(payload.keys())
        vals = list(payload.values())
        insert_or_ignore(cursor, 'event_shot', cols,vals)