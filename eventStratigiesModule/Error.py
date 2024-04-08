from db_events_setup import insert_or_ignore


id = 37
class Strategy:
    def handle(self, cursor, payload):
        event_id = payload.get('id', None)
        event_player = payload.get('player', None).get('id', None)
        event_position = payload.get('position', None).get('name', None)
        event_location_x = payload.get('location', None)[0]
        event_location_y = payload.get('location', None)[1]
        event_duration = payload.get('duration', None)
        event_under_pressure = payload.get('under_pressure', None)
        event_off_camera = payload.get('off_camera', None)

        insert_or_ignore(cursor, 'event_error', ['event_id', 'event_player', 'event_position', 'event_location_x', 'event_location_y', 'event_duration', 'event_under_pressure', 'event_off_camera'], [event_id, event_player, event_position, event_location_x, event_location_y, event_duration, event_under_pressure, event_off_camera])