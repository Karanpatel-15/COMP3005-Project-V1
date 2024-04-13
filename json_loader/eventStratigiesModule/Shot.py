
from db_events_setup import insert_or_ignore

# {
#     "id": "1fcda1a4-23c9-42df-8153-6c6142fcc3c7",
#     "index": 387,
#     "period": 1,
#     "timestamp": "00:06:33.123",
#     "minute": 6,
#     "second": 33,
#     "type": {
#       "id": 16,
#       "name": "Shot"
#     },
#     "possession": 17,
#     "possession_team": {
#       "id": 217,
#       "name": "Barcelona"
#     },
#     "play_pattern": {
#       "id": 4,
#       "name": "From Throw In"
#     },
#     "team": {
#       "id": 217,
#       "name": "Barcelona"
#     },
#     "player": {
#       "id": 5503,
#       "name": "Lionel Andrés Messi Cuccittini"
#     },
#     "position": {
#       "id": 23,
#       "name": "Center Forward"
#     },
#     "location": [103.3, 51.7],
#     "duration": 1.188,
#     "related_events": ["ce77e40f-d09a-4aa6-aa27-092f4f337b69"],
#     "shot": {
#       "statsbomb_xg": 0.053563748,
#       "end_location": [120.0, 35.2, 3.4],
#       "key_pass_id": "8a2fe20c-4e50-4a02-b518-a94ffd7bbc88",
#       "technique": {
#         "id": 93,
#         "name": "Normal"
#       },
#       "outcome": {
#         "id": 98,
#         "name": "Off T"
#       },
#       "type": {
#         "id": 87,
#         "name": "Open Play"
#       },
#       "body_part": {
#         "id": 38,
#         "name": "Left Foot"
#       }
#     }
#   }

id = 16
class Strategy:
    def handle(self,cursor,payload):
        # SELECT event_id, event_player_id, event_player_name, event_season_id, event_competition_id, event_position, event_team_id, event_location_x, event_location_y, event_duration, event_out, event_under_pressure, event_off_camera, event_statsbomb_xg, end_location_x, end_location_y, event_body_part, event_outcome, event_first_time, event_technique, event_deflected, event_one_on_one, event_aerial_won, event_saved_to_post, event_redirect, event_open_goal, event_follows_dribble, event_saved_off_target

#         export interface Shot {
#     id: string;
#     index: number;
#     period: number;
#     timestamp: string;
#     minute: number;
#     second: number;
#     type: Foreign;
#     possession: number;
#     possession_team: Foreign;
#     play_pattern: Foreign;
#     team: Foreign;
#     player: Foreign;
#     position: Foreign;
#     location: number[];
#     duration: number;
#     shot: ShotClass;
#     under_pressure: boolean;
#     out: boolean;
#     off_camera: boolean;
# }

# export interface Foreign {
#     id: number;
#     name: string;
# }

# export interface ShotClass {
#     statsbomb_xg: number;
#     end_location: number[];
#     key_pass_id: string | null;
#     body_part: Foreign;
#     type: Foreign;
#     outcome: Foreign;
#     first_time: boolean;
#     technique: Foreign;
#     freeze_frame: FreezeFrame[] | null;
#     deflected: boolean;
#     one_on_one: boolean;
#     aerial_won: boolean;
#     saved_to_post: boolean;
#     redirect: boolean;
#     open_goal: boolean;
#     follows_dribble: boolean;
#     saved_off_target: boolean;
# }
        shot_payload = payload.get('shot', {})
        event_id = payload.get('id', None)
        competition_id = payload.get('competition_id')
        season_id = payload.get('season_id')
        event_team_id = payload.get('team', {}).get('id', None)
        event_team_name = payload.get('team', {}).get('name', None)
        player_id = payload.get('player').get('id', None)
        event_player_name = payload.get('player', None).get('name', None)
        event_position = payload.get('position', {}).get('name', None)
        event_location_x = payload.get('location', [0, 0])[0]
        event_location_y = payload.get('location', [0, 0])[1]
        event_duration = payload.get('duration', None)
        event_out = payload.get("out", None)
        event_under_pressure = payload.get("under_pressure", None)
        event_off_camera = payload.get("off_camera", None)
        event_statsbomb_xg = shot_payload.get('statsbomb_xg')
        end_location_x = shot_payload.get('end_location', [0, 0, 0])[0]
        end_location_y = shot_payload.get('end_location', [0, 0, 0])[1]
        event_first_time = shot_payload.get('first_time')
        # TODO: Add more fields

        upsertPayload = {
            "event_id": event_id,
            "event_player_id": player_id,
            "event_player_name": event_player_name,
            "event_statsbomb_xg": event_statsbomb_xg,
            "event_first_time": event_first_time,
            "event_competition_id": competition_id,
            "event_season_id": season_id,
            "event_position": event_position,
            "event_team_id": event_team_id,
            "event_team_name": event_team_name,
            "event_location_x": event_location_x,
            "event_location_y": event_location_y,
            "event_duration": event_duration,
            "event_out": event_out,
            "event_under_pressure": event_under_pressure,
            "event_off_camera": event_off_camera,
            "end_location_x": end_location_x,
            "end_location_y": end_location_y
            
        }
        cols = list(upsertPayload.keys())
        vals = list(upsertPayload.values())
        insert_or_ignore(cursor, 'event_shot', cols,vals)