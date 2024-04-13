from db_events_setup import insert_or_ignore

id = 30
class Strategy:
    def handle(self, cursor, payload):
        # print("Inserting Pass  " + str(payload))
        pass_payload = payload.get("pass", {})

        upsertPayload =  {
            "event_id": payload.get("id", None),
            "event_season_id": payload.get("season_id", None),
            "event_competition_id": payload.get("competition_id", None),
            "event_player_id" : payload.get("player", {}).get("id", None),
            "team_id": payload.get("team", {}).get("id", None),
            "CID_SID": str(payload.get("competition_id", None)) + "_" + str(payload.get("season_id", None)),
            "team_name": payload.get("team", {}).get("name", None),
            "event_recipient_id" : pass_payload.get("recipient", {}).get("id", None),
            "length" : pass_payload.get("length", None),
            "event_recipient_id" : pass_payload.get("recipient", {}).get("id", None),
            "length" : pass_payload.get("length", None),
            "angle": pass_payload.get("angle", None),
            "height" : pass_payload.get("height", {}).get("name", None),
            "end_location_x" : pass_payload.get("end_location", [0, 0])[0],
            "end_location_y" : pass_payload.get("end_location", [0, 0])[1],
            "backheel" : pass_payload.get("backheel", False),
            "deflected" : pass_payload.get("deflected", False),
            "miscommunication" : pass_payload.get("miscommunication", False),
            "is_cross" : pass_payload.get("cross", False),
            "cutback" : pass_payload.get("cut_back", False),
            "switch" :  pass_payload.get("switch", False),
            "shot_assist" : pass_payload.get("shot_assist", False),
            "goal_assist" : pass_payload.get("goal_assist", False),
            "body_part" : pass_payload.get("body_part", {}).get("name", None),
            "type" : pass_payload.get("type", {}).get("name", None),
            "outcome" : pass_payload.get("outcome", {}).get("name", None),
            "technique" : pass_payload.get("technique", {}).get("name", None),
        }
        cols = upsertPayload.keys()
        vals = list(upsertPayload.values())
        insert_or_ignore(cursor, "event_pass",cols, vals)






        

