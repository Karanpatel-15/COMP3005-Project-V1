from db_events_setup import insert_or_ignore

id = 24

class Strategy:
    def handle(self, cursor, payload):
        bad_behaviour = payload.get('bad_behaviour', {})
        card = bad_behaviour.get('card', {})
        upsertPayload = {
            "event_id": payload.get('id', None),
            "event_player": payload.get('player', None).get('id', None),
            "event_position": payload.get('position', {}).get('name', None),
            "event_team_id": payload.get('team', {}).get('id', None),
            "event_location_x": payload.get('location', [None, None])[0],
            "event_location_y": payload.get('location', [None, None])[1],
            "event_timestamp": payload.get('timestamp', None),
            "event_duration": payload.get('duration', None),
            "event_off_camera": payload.get('off_camera', None),
            "event_card_type": card.get('name', None)
        }
        cols = upsertPayload.keys()
        vals = list(upsertPayload.values())
        insert_or_ignore(cursor, 'event_bad_behaviour', cols, vals)