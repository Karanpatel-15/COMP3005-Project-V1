from db_events_setup import insert_or_ignore
# "id" : "72c3344a-c828-42f0-a7e5-61fae10b361e",
#   "index" : 5,
#   "period" : 1,
#   "timestamp" : "00:00:01.430",
#   "minute" : 0,
#   "second" : 1,
#   "type" : {
#     "id" : 30,
#     "name" : "Pass"
#   },
#   "possession" : 2,
#   "possession_team" : {
#     "id" : 972,
#     "name" : "West Ham United LFC"
#   },
#   "play_pattern" : {
#     "id" : 9,
#     "name" : "From Kick Off"
#   },
#   "team" : {
#     "id" : 972,
#     "name" : "West Ham United LFC"
#   },
#   "player" : {
#     "id" : 4653,
#     "name" : "Jane Ross"
#   },
#   "position" : {
#     "id" : 22,
#     "name" : "Right Center Forward"
#   },
#   "location" : [ 61.0, 41.0 ],
#   "duration" : 2.264,
#   "related_events" : [ "f9158c21-39ce-46ce-94b8-9b7aa70ab13a" ],
#   "pass" : {
#     "recipient" : {
#       "id" : 18159,
#       "name" : "Brooke Hendrix"
#     },
#     "length" : 23.086792,
#     "angle" : 2.83354,
#     "height" : {
#       "id" : 1,
#       "name" : "Ground Pass"
#     },
#     "end_location" : [ 39.0, 48.0 ],
#     "body_part" : {
#       "id" : 40,
#       "name" : "Right Foot"
#     },
#     "type" : {
#       "id" : 65,
#       "name" : "Kick Off"
#     }
#   }

id = 30
class Strategy:
    def handle(self, cursor, payload):
        print("Inserting Error  " + str(payload))

        event_id = payload.get('id', None)
        event_player = payload.get('player', None).get('id', None)
        event_position = payload.get('position', None).get('name', None)
        event_location_x = payload.get('location', None)[0]
        event_location_y = payload.get('location', None)[1]
        event_duration = payload.get('duration', None)
        event_under_pressure = payload.get('under_pressure', None)
        event_off_camera = payload.get('off_camera', None)

