from db_events_setup import insert_or_ignore


id = 22
class Strategy:
    def handle(self, cursor, payload):
        print("Inserting Foul Committed  " + str(payload))

        # CREATE TABLE IF NOT EXISTS foul (
        #     event_id UUID,
        #     penalty BOOLEAN,
        #     advantage BOOLEAN,
        #     card_id INTEGER,
        #     offensive BOOLEAN,
        #     FOREIGN KEY (event_id) REFERENCES event(event_id),
        #     FOREIGN KEY (card_id) REFERENCES card(card_id),
        #     UNIQUE (event_id)
        # );

        # CREATE TABLE IF NOT EXISTS event_foul_committed (
        #     event_id UUID,
        #     event_player INTEGER,
        #     event_position VARCHAR(100),
        #     event_location_x FLOAT,
        #     event_location_y FLOAT,
        #     event_duration FLOAT,
        #     event_counterpress BOOLEAN,
        #     off_camera BOOLEAN,
        #     under_pressure BOOLEAN,
        #     FOREIGN KEY (event_id) REFERENCES event(event_id),
        #     FOREIGN KEY (event_player) REFERENCES player(player_id),
        #     UNIQUE (event_id)
        # );

        # {
        #     "id": "95bb114f-02f5-4e95-8b1c-9c400b6377d2",
        #     "index": 3007,
        #     "period": 2,
        #     "timestamp": "00:19:13.940",
        #     "minute": 64,
        #     "second": 13,
        #     "type": {
        #     "id": 22,
        #     "name": "Foul Committed"
        #     },
        #     "possession": 135,
        #     "possession_team": {
        #     "id": 222,
        #     "name": "Villarreal"
        #     },
        #     "play_pattern": {
        #     "id": 1,
        #     "name": "Regular Play"
        #     },
        #     "team": {
        #     "id": 217,
        #     "name": "Barcelona"
        #     },
        #     "player": {
        #     "id": 6332,
        #     "name": "Thomas Vermaelen"
        #     },
        #     "position": {
        #     "id": 5,
        #     "name": "Left Center Back"
        #     },
        #     "location": [53.0, 52.0],
        #     "duration": 0.0,
        #     "related_events": [
        #     "0317f476-4fb0-40d5-9d2b-43dcb562fa7d",
        #     "f94d9b23-f385-4c77-831e-805b84fc2fc6"
        #     ],
        #     "foul_committed": {
        #     "advantage": true
        #     }
        # }

        event_id = payload.get('id', None)
        event_player = payload.get('player', None).get('id', None)
        event_position = payload.get('position', None).get('name', None)
        event_location_x = payload.get('location', None)[0]
        event_location_y = payload.get('location', None)[1]
        event_duration = payload.get('duration', None)
        event_counterpress = payload.get('counterpress', None)
        event_off_camera = payload.get('off_camera', None)
        event_under_pressure = payload.get('under_pressure', None)

        foul_committed = payload.get('foul_committed', None)
        
        if foul_committed is not None:
            penalty = foul_committed.get('penalty', None)
            advantage = foul_committed.get('advantage', None)
            card = foul_committed.get('card', None)
            card_id = None
            if card is not None:
                card_id = card.get('name', None)
            offensive = foul_committed.get('offensive', None)
            insert_or_ignore(cursor, 'foul', ['event_id', 'penalty', 'advantage', 'card_id', 'offensive'], [event_id, penalty, advantage, card_id, offensive])

        insert_or_ignore(cursor, 'event_foul_committed', ['event_id', 'event_player', 'event_position', 'event_location_x', 'event_location_y', 'event_duration', 'event_counterpress', 'off_camera', 'under_pressure'], [event_id, event_player, event_position, event_location_x, event_location_y, event_duration, event_counterpress, event_off_camera, event_under_pressure])