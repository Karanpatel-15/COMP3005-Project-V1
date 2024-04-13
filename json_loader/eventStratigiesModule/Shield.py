from db_events_setup import insert_or_ignore

id = 28  # Event type ID for "Shield"

class Strategy:
    def handle(self, cursor, payload):
        # Extracting relevant data from the payload
        event_id = payload.get('id', None)
        event_location_x = payload.get('location', [None, None])[0]
        event_location_y = payload.get('location', [None, None])[1]

        # Constructing the payload for insertion
        upsertPayload = {
            "event_id": event_id,
            "event_location_x": event_location_x,
            "event_location_y": event_location_y,
        }

        # Extracting column names and values
        cols = upsertPayload.keys()
        vals = list(upsertPayload.values())

        # Inserting or ignoring based on event_id uniqueness constraint
        insert_or_ignore(cursor, 'event_shield', cols, vals)
