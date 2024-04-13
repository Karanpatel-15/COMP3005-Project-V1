from db_events_setup import insert_or_ignore

id = 21
class Strategy:
    def handle(self, cursor, payload):
        foul_won = payload.get('foul_won', {})
        upsertPayload = {
            "event_id": payload.get('id', None),
            "event_player": payload.get('player', {}).get('id', None),
            "event_position": payload.get('position', {}).get('name', None),
            "event_location_x": payload.get('location', [None, None])[0],
            "event_location_y": payload.get('location', [None, None])[1],
            "event_duration": payload.get('duration', None),
            "event_under_pressure": payload.get('under_pressure', None),
            "event_off_camera": payload.get('off_camera', None),
            "event_penalty": foul_won.get('penalty', None),
            "event_defensive": foul_won.get('defensive', None),
            "event_advantage": foul_won.get('advantage', None)
        }
        cols = upsertPayload.keys()
        vals = list(upsertPayload.values())
        insert_or_ignore(cursor, 'event_foul_won', cols, vals)
