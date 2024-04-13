from db_events_setup import insert_or_ignore

id = 19  # Event type ID for "Substitution"

class Strategy:
    def handle(self, cursor, payload):
        # Extracting relevant data from the payload
        event_id = payload.get('id', None)
        player_id = payload.get('player', {}).get('id', None)
        replacement_id = payload.get('substitution', {}).get('replacement', {}).get('id', None)
        duration = payload.get('duration', None)

        # Constructing the payload for insertion
        upsertPayload = {
            "event_id": event_id,
            "event_player_id": player_id,
            "event_player_replacement_id": replacement_id,
            "event_duration" : duration,
        }

        # Extracting column names and values
        cols = upsertPayload.keys()
        vals = list(upsertPayload.values())

        # Inserting or ignoring based on event_id uniqueness constraint
        insert_or_ignore(cursor, 'event_substitution', cols, vals)