from db_events_setup import insert_or_ignore

id = 38  # Event type ID for "Miscontrol"

class Strategy:
    def handle(self, cursor, payload):
        # Extracting relevant data from the payload
        event_id = payload.get('id', None)
        event_player_id = payload.get('player', {}).get('id', None)
        event_position = payload.get('position', {}).get('name', None)
        event_team_id = payload.get('team', {}).get('id', None)
        event_location_x = payload.get('location', [None, None])[0]
        event_location_y = payload.get('location', [None, None])[1]
        event_duration = payload.get('duration', None)
        event_out = payload.get('out', None)
        event_under_pressure = payload.get('under_pressure', None)
        event_aerial_won = payload.get('aerial_won', None)
        event_off_camera = payload.get('off_camera', None)

        # Constructing the payload for insertion
        upsertPayload = {
            "event_id": event_id,
            "event_player": event_player_id,
            "event_position": event_position,
            "event_team_id": event_team_id,
            "event_location_x": event_location_x,
            "event_location_y": event_location_y,
            "event_duration": event_duration,
            "event_out": event_out,
            "event_under_pressure": event_under_pressure,
            "event_aerial_won": event_aerial_won,
            "event_off_camera": event_off_camera
        }

        # Extracting column names and values
        cols = upsertPayload.keys()
        vals = list(upsertPayload.values())

        # Insertin
