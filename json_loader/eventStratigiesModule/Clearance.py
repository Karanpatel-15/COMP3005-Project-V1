from db_events_setup import insert_or_ignore

id = 9

class Strategy:
    def handle(self, cursor, payload):
        clearance = payload.get('clearance', {})
        body_part = clearance.get('body_part', {})
        
        upsertPayload = {
            "event_id": payload.get('id', None),
            "event_player": payload.get('player', None).get('id', None),
            "event_position": payload.get('position', {}).get('name', None),
            "event_team_id": payload.get('team', {}).get('id', None),
            "event_location_x": payload.get('location', [None, None])[0],
            "event_location_y": payload.get('location', [None, None])[1],
            "event_duration": payload.get('duration', None),
            "event_out": payload.get('out', None),
            "event_off_camera": payload.get('off_camera', None),
            "event_right_foot": clearance.get('right_foot', None),
            "event_left_foot": clearance.get('left_foot', None),
            "event_body_part": body_part.get('name', None),
            "event_aerial_won": clearance.get('aerial_won', None),
            "event_head": clearance.get('head', None),
        }
        cols = upsertPayload.keys()
        vals = list(upsertPayload.values())
        insert_or_ignore(cursor, 'event_clearance', cols, vals)
