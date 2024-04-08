from db_events_setup import insert_or_ignore

id = 30
class Strategy:
    def handle(self, cursor, payload):
        # print("Inserting Pass  " + str(payload))

        event_id = payload.get("id", None)
        event_player = payload.get("player", {}).get("id", None)
        event_position = payload.get("position", {}).get("name", None)
        event_location_x = payload.get("location", [None, None])[0]
        event_location_y = payload.get("location", [None, None])[1]
        event_duration = payload.get("duration", None)
        event_under_pressure = payload.get("under_pressure", None)
        event_off_camera = payload.get("off_camera", None)
        event_counterpress = payload.get("counterpress", None)
        event_out = payload.get("out", None)
        
        pass_payload = payload.get("pass", {})
        event_recipient_id = pass_payload.get("recipient", {}).get("id", None)
        event_length = pass_payload.get("length", None)
        event_angle = pass_payload.get("angle", None)
        event_height = pass_payload.get("height", {}).get("name", None)
        event_end_location_x = pass_payload.get("end_location", [None, None])[0]
        event_end_location_y = pass_payload.get("end_location", [None, None])[1]
        event_body_part = pass_payload.get("body_part", {}).get("name", None)
        event_type = pass_payload.get("type", {}).get("name", None)
        event_outcome = pass_payload.get("outcome", {}).get("name", None)
        event_aerial_won = pass_payload.get("aerial_won", None)
        event_shot_assist = pass_payload.get("shot_assist", None)
        event_switch = pass_payload.get("switch", None)
        event_cross = pass_payload.get("cross", None)
        event_deflected = pass_payload.get("deflected", None)
        event_inswinging = pass_payload.get("inswinging", None)
        event_technique = pass_payload.get("technique", {}).get("name", None)
        event_through_ball = pass_payload.get("through_ball", None)
        event_no_touch = pass_payload.get("no_touch", None)
        event_outswinging = pass_payload.get("outswinging", None)
        event_miscommunication = pass_payload.get("miscommunication", None)
        event_cut_back = pass_payload.get("cut_back", None)
        event_goal_assist = pass_payload.get("goal_assist", None)
        event_straight = pass_payload.get("straight", None)

        cols = ["event_id", "event_player", "event_position", "event_location_x", "event_location_y", "event_duration", "event_under_pressure", "event_off_camera", "event_counterpress", "event_out", "event_recipient_id", "event_length", "event_angle", "event_height", "event_end_location_x", "event_end_location_y", "event_body_part", "event_type", "event_outcome", "event_aerial_won", "event_shot_assist", "event_switch", "event_cross", "event_deflected", "event_inswinging", "event_technique", "event_through_ball", "event_no_touch", "event_outswinging", "event_miscommunication", "event_cut_back", "event_goal_assist", "event_straight"] 
        vals = [event_id, event_player, event_position, event_location_x, event_location_y, event_duration, event_under_pressure, event_off_camera, event_counterpress, event_out, event_recipient_id, event_length, event_angle, event_height, event_end_location_x, event_end_location_y, event_body_part, event_type, event_outcome, event_aerial_won, event_shot_assist, event_switch, event_cross, event_deflected, event_inswinging, event_technique, event_through_ball, event_no_touch, event_outswinging, event_miscommunication, event_cut_back, event_goal_assist, event_straight]
        insert_or_ignore(cursor, "event_pass",cols, vals)






        

