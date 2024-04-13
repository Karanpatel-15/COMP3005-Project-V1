from db_events_setup import insert_or_ignore

id = 34
class Strategy:
    def handle(self, cursor, payload):
        half_end = payload.get('half_end', {})
        upsertPayload = {
            "event_id": payload.get('id', None),
            "event_duration": payload.get('duration', None),
            "event_under_pressure": payload.get('under_pressure', None)
        }
        cols = upsertPayload.keys()
        vals = list(upsertPayload.values())
        insert_or_ignore(cursor, 'event_half_end', cols, vals)
