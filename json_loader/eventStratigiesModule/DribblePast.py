from db_events_setup import insert_or_ignore

id = 39
class Strategy:
    def handle(self, cursor, payload):
        upsertPayload = {
        "event_id" : payload.get('id', None),
        "event_player_id" : payload.get('player', {}).get('id', None),
        "event_player_name": payload.get('player', {}).get('name', None),
        "event_competition_id" : payload.get('competition_id', None),
        "event_season_id" : payload.get('season_id', None),
        "event_position": payload.get('position', None).get('name', None),
        "event_location_x": payload.get('location', [None, None])[0],
        "event_location_y": payload.get('location', [None, None])[1],
        "event_duration" : payload.get('duration', None),
        "event_counterpress" : payload.get('counterpress', None),
        "event_off_camera" : payload.get('off_camera', None),
        "event_competition_id" : payload.get('competition_id', None),
        "event_player_id" : payload.get('player', {}).get('id', None),
        }

        cols = upsertPayload.keys()
        vals = list(upsertPayload.values())

        insert_or_ignore(cursor, 'event_dribbled_past', cols, vals)
