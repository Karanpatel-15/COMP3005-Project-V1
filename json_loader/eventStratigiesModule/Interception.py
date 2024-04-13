from db_events_setup import insert_or_ignore

id = 10  # Event type ID for "Interception"

class Strategy:
    def handle(self, cursor, payload):
        # Extracting relevant data from the payload
        event_id = payload.get('id', None)
        event_player_id = payload.get('player', {}).get('id', None)
        event_position = payload.get('position', {}).get('name', None)
        event_team_id = payload.get('team', {}).get('id', None)
        event_location_x = payload.get('location', [None, None])[0]
        event_location_y = payload.get('location', [None, None])[1]
        event_interception_outcome = payload.get('interception', {}).get('outcome', {}).get('name', None)
        event_counterpress = payload.get('counterpress', None)
        event_duration = payload.get('duration', None)
        event_outcome = payload.get('interception', {}).get('outcome', {}).get('name', None)

        # Constructing the payload for insertion
        upsertPayload = {
            "event_id": event_id,
            "event_player": event_player_id,
            "event_position": event_position,
            "event_location_x": event_location_x,
            "event_location_y": event_location_y,
            "event_duration": event_duration,
            "event_interception_outcome": event_interception_outcome,
            "event_counterpress": event_counterpress,
            "event_outcome": event_outcome,
            "event_under_pressure": payload.get('under_pressure', None)
        }

        # Extracting column names and values
        cols = upsertPayload.keys()
        vals = list(upsertPayload.values())

        # Inserting or ignoring based on event_id uniqueness constraint
        insert_or_ignore(cursor, 'event_interception', cols, vals)