from db_events_setup import insert_or_ignore

id = 43

class Strategy:
    def handle(self, cursor, payload):
        carry = payload.get('carry', {})
        upsertPayload = {
            "event_id": payload.get('id', None),
            "event_player": payload.get('player', None).get('id', None),
            "event_position": payload.get('position', {}).get('name', None),
            "event_team_id": payload.get('team', {}).get('id', None),
            "event_location_x": payload.get('location', [None, None])[0],
            "event_location_y": payload.get('location', [None, None])[1],
            "event_duration": payload.get('duration', None),
            "event_under_pressure": payload.get('under_pressure', None),
            "end_location_x": carry.get('end_location', [None, None])[0],
            "end_location_y": carry.get('end_location', [None, None])[1]
        }
        cols = upsertPayload.keys()
        vals = list(upsertPayload.values())
        insert_or_ignore(cursor, 'event_carry', cols, vals)
