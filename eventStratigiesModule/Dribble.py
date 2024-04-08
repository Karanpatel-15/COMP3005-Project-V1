from db_events_setup import insert_or_ignore


id = 14
class Strategy:
    def handle(self, cursor, payload):
        event_id = payload.get('id', None)
        event_player = payload.get('player', None).get('id', None)
        event_position = payload.get('position', None).get('name', None)
        event_location_x = payload.get('location', [None, None])[0]
        event_location_y = payload.get('location', [None, None])[1]
        event_duration = payload.get('duration', None)
        event_under_pressure = payload.get('under_pressure', None)
        event_off_camera = payload.get('off_camera', None)
        event_out = payload.get('out', None)
        event_outcome = payload.get('dribble', {}).get('outcome', None).get('name', None)
        event_overrun = payload.get('dribble', {}).get('overrun', None)
        event_nutmeg = payload.get('dribble', {}).get('nutmeg', None)
        event_no_touch = payload.get('dribble', {}).get('no_touch', None)

        cols = ['event_id', 'event_player', 'event_position', 'event_location_x', 'event_location_y', 'event_duration', 'event_under_pressure', 'event_off_camera', 'event_out', 'event_outcome', 'event_overrun', 'event_nutmeg', 'event_no_touch']
        vals = [event_id, event_player, event_position, event_location_x, event_location_y, event_duration, event_under_pressure, event_off_camera, event_out, event_outcome, event_overrun, event_nutmeg, event_no_touch]

        insert_or_ignore(cursor, 'event_dribble', cols, vals)