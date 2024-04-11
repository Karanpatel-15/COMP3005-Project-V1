from db_events_setup import insert_or_ignore


id = 14
class Strategy:
    def handle(self, cursor, payload):
        dribble = payload.get('dribble', {})
        upsertPayload = {
        "event_id" : payload.get('id', None),
        "event_player" : payload.get('player', None).get('id', None),
        "overrun" : dribble.get('overrun', False),
        "nutmeg" : dribble.get('nutmeg', False),
        "outcome" : dribble.get('outcome', {}).get('name', None),
        "no_touch" : dribble.get('no_touch', False)
        }
        cols = upsertPayload.keys()
        vals = list(upsertPayload.values())
        insert_or_ignore(cursor, 'event_dribble', cols, vals)