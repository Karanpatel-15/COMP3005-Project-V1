from db_events_setup import insert_or_ignore

id = 27  # Event type ID for "Player Off"

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
        event_off_camera = payload.get('off_camera', None)

        # Constructing the payload for insertion
        upsertPayload = {
            "event_id": event_id,
            "event_player": event_player_id,
            "event_position": event_position,
            "event_location_x": event_location_x,
            "event_location_y": event_location_y,
            "event_duration": event_duration,
            "event_off_camera": event_off_camera
        }

        # Extracting column names and values
        cols = upsertPayload.keys()
        vals = list(upsertPayload.values())

        # Inserting or ignoring based on event_id uniqueness constraint
        insert_or_ignore(cursor, 'event_playerOff', cols, vals)
