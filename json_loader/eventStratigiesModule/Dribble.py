from db_events_setup import insert_or_ignore

id = 14
class Strategy:
    def handle(self, cursor, payload):
        dribble = payload.get('dribble', {})
        upsertPayload = {
        "event_id" : payload.get('id', None),
        "event_player_id" : payload.get('player', None).get('id', None),
        "event_player_name": payload.get('player', {}).get('name', None),
        "event_location_x" : payload.get('location', [None, None])[0],
        "event_competition_id" : payload.get('competition_id', None),
        "event_season_id" : payload.get('season_id', None),
        "event_location_y" : payload.get('location', [None, None])[1],
        "event_position" : payload.get('position', {}).get('name', None),
        "event_duration" : payload.get('duration', None),
        "event_under_pressure" : payload.get('under_pressure', None),
        "event_off_camera" : payload.get('off_camera', None),
        "event_out" : payload.get('out', None),
        "event_outcome" : dribble.get('outcome', {}).get('name', None),
        "event_overrun" : dribble.get('overrun', None),
        "event_nutmeg" : dribble.get('nutmeg', None),
        "event_no_touch" : dribble.get('no_touch', None)
        }
        cols = upsertPayload.keys()
        vals = list(upsertPayload.values())
        insert_or_ignore(cursor, 'event_dribble', cols, vals)