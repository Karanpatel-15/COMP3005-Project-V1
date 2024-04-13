DROP SCHEMA public CASCADE;
CREATE SCHEMA public;


CREATE TABLE IF NOT EXISTS season (
    season_id INTEGER PRIMARY KEY,
    season_name VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS manager (
    manager_id INTEGER PRIMARY KEY,
    manager_name VARCHAR(100),
    manager_nickname VARCHAR(100),
    manager_dob DATE,
    country_name VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS referee (
    referee_id INTEGER PRIMARY KEY,
    referee_name VARCHAR(100),
    country_name VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS competition (
    competition_id INTEGER PRIMARY KEY,
    country_name VARCHAR(50),
    competition_name VARCHAR(100),
    competition_gender VARCHAR(50),
    competition_youth BOOLEAN,
    competition_international BOOLEAN
);

CREATE TABLE IF NOT EXISTS competition_season (
    competition_id INTEGER,
    season_id INTEGER,
    FOREIGN KEY (competition_id) REFERENCES competition(competition_id),
    FOREIGN KEY (season_id) REFERENCES season(season_id),
    UNIQUE (competition_id, season_id)
);

CREATE TABLE IF NOT EXISTS stadium (
    stadium_id INTEGER PRIMARY KEY,
    stadium_name VARCHAR(100),
    country_name VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS team (
    team_id INTEGER PRIMARY KEY,
    team_name VARCHAR(100),
    team_gender VARCHAR(50),
    country_name VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS match (
    match_id INTEGER PRIMARY KEY,
    match_date DATE,
    kick_off TIME,
    stadium_id INTEGER,
    referee_id INTEGER,
    home_team_id INTEGER,
    away_team_id INTEGER,
    home_score INTEGER,
    away_score INTEGER,
    match_status VARCHAR(100),
    match_week INTEGER,
    competition_stage VARCHAR(100),
    competition_id INTEGER,
    season_id INTEGER,
    FOREIGN KEY (stadium_id) REFERENCES stadium(stadium_id),
    FOREIGN KEY (referee_id) REFERENCES referee(referee_id),
    FOREIGN KEY (competition_id) REFERENCES competition(competition_id),
    FOREIGN KEY (season_id) REFERENCES season(season_id),
    FOREIGN KEY (home_team_id) REFERENCES team(team_id),
    FOREIGN KEY (away_team_id) REFERENCES team(team_id)
);

CREATE TABLE IF NOT EXISTS team_manager (
    team_id INTEGER,
    manager_id INTEGER,
    FOREIGN KEY (team_id) REFERENCES team(team_id),
    FOREIGN KEY (manager_id) REFERENCES manager(manager_id),
    UNIQUE (team_id, manager_id)
);

CREATE TABLE IF NOT EXISTS player (
    player_id INTEGER PRIMARY KEY,
    player_name VARCHAR(255),
    player_nickname VARCHAR(255),
    jersey_number INTEGER,
    country_name VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS lineup (
    match_id INTEGER,
    team_id INTEGER,
    player_id INTEGER,
    FOREIGN KEY (match_id) REFERENCES match(match_id),
    FOREIGN KEY (team_id) REFERENCES team(team_id),
    FOREIGN KEY (player_id) REFERENCES player(player_id),
    UNIQUE (match_id, team_id, player_id)
);

CREATE TABLE IF NOT EXISTS position (
    position_id INTEGER PRIMARY KEY,
    player_id INTEGER,
    match_id INTEGER,
    position VARCHAR(255),
    from_time VARCHAR(10),
    to_time VARCHAR(10),
    from_period INTEGER,
    to_period INTEGER,
    start_reason VARCHAR(255),
    end_reason VARCHAR(255),
    FOREIGN KEY (player_id) REFERENCES player(player_id),
    FOREIGN KEY (match_id) REFERENCES match(match_id)
);

CREATE TABLE IF NOT EXISTS card (
    card_id SERIAL PRIMARY KEY,
    player_id INTEGER,
    match_id INTEGER,
    card_time VARCHAR(10),
    card_type VARCHAR(255),
    card_reason VARCHAR(255),
    card_period INTEGER,
    period INTEGER,
    FOREIGN KEY (player_id) REFERENCES player(player_id),
    FOREIGN KEY (match_id) REFERENCES match(match_id)
);

CREATE TABLE IF NOT EXISTS event (
    event_id UUID PRIMARY KEY,
    event_index INTEGER,
    event_period INTEGER,
    event_timestamp VARCHAR(20),
    event_minute INTEGER,
    event_second INTEGER,
    event_type VARCHAR(100),
    event_possession INTEGER,
    event_possession_team_id INTEGER,
    event_play_pattern VARCHAR(100),
    event_team_id INTEGER,
    FOREIGN KEY (event_possession_team_id) REFERENCES team(team_id),
    FOREIGN KEY (event_team_id) REFERENCES team(team_id)
);

CREATE TABLE IF NOT EXISTS match_event (
    match_id INTEGER,
    event_id UUID,
    FOREIGN KEY (event_id) REFERENCES event(event_id),
    FOREIGN KEY (match_id) REFERENCES match(match_id),
    UNIQUE (event_id, match_id)
);

CREATE TABLE IF NOT EXISTS competition_season_event_mapping (
    season_id INTEGER,
    competition_id INTEGER,
    event_id UUID,
    FOREIGN KEY (season_id) REFERENCES season(season_id),
    FOREIGN KEY (event_id) REFERENCES event(event_id),
    PRIMARY KEY (season_id, competition_id, event_id),
    UNIQUE (season_id, event_id)
);

-- ___________ Rayyan ___________ (5050 to Duel)

CREATE TABLE IF NOT EXISTS event_bad_behaviour (
    event_id UUID,
    event_player INTEGER,
    event_position VARCHAR(100),
    event_team_id INTEGER,
    event_location_x FLOAT,
    event_location_y FLOAT,
    event_timestamp VARCHAR(20),
    event_duration FLOAT,
    event_off_camera BOOLEAN,
    event_card_type VARCHAR(100),
    FOREIGN KEY (event_id) REFERENCES event(event_id),
    FOREIGN KEY (event_player) REFERENCES player(player_id),
    FOREIGN KEY (event_team_id) REFERENCES team(team_id),
    UNIQUE (event_id)
);

CREATE TABLE IF NOT EXISTS event_ball_receipt (
    event_id UUID,
    event_player INTEGER,
    event_position VARCHAR(100),
    event_possession_team_id INTEGER,
    event_timestamp VARCHAR(20),
    event_location_x FLOAT,
    event_location_y FLOAT,
    event_under_pressure BOOLEAN,
    event_outcome VARCHAR(100),
    FOREIGN KEY (event_id) REFERENCES event(event_id),
    FOREIGN KEY (event_player) REFERENCES player(player_id),
    FOREIGN KEY (event_possession_team_id) REFERENCES team(team_id),
    UNIQUE (event_id)
);

CREATE TABLE IF NOT EXISTS event_ball_recovery (
    event_id UUID,
    event_player INTEGER,
    event_position VARCHAR(100),
    event_possession_team_id INTEGER,
    event_timestamp VARCHAR(20),
    event_location_x FLOAT,
    event_location_y FLOAT,
    event_under_pressure BOOLEAN,
    event_recovery_failure BOOLEAN,
    event_offensive BOOLEAN,
    event_off_camera BOOLEAN,
    FOREIGN KEY (event_id) REFERENCES event(event_id),
    FOREIGN KEY (event_player) REFERENCES player(player_id),
    FOREIGN KEY (event_possession_team_id) REFERENCES team(team_id),
    UNIQUE (event_id)
);

CREATE TABLE IF NOT EXISTS event_block (
    event_id UUID,
    event_player INTEGER,
    event_position VARCHAR(100),
    event_possession_team_id INTEGER,
    event_timestamp VARCHAR(20),
    event_location_x FLOAT,
    event_location_y FLOAT,
    event_under_pressure BOOLEAN,
    event_off_camera BOOLEAN,
    event_counterpress  BOOLEAN,
    event_deflection BOOLEAN,
    event_offensive BOOLEAN,
    event_save_block BOOLEAN,
    FOREIGN KEY (event_id) REFERENCES event(event_id),
    FOREIGN KEY (event_player) REFERENCES player(player_id),
    FOREIGN KEY (event_possession_team_id) REFERENCES team(team_id),
    UNIQUE (event_id)
);

CREATE TABLE IF NOT EXISTS event_carry (
    event_id UUID,
    event_player INTEGER,
    event_position VARCHAR(100),
    event_team_id INTEGER,
    event_location_x FLOAT,
    event_location_y FLOAT,
    event_duration FLOAT,
    event_under_pressure BOOLEAN,
    end_location_x FLOAT,
    end_location_y FLOAT,
    FOREIGN KEY (event_id) REFERENCES event(event_id),
    FOREIGN KEY (event_player) REFERENCES player(player_id),
    FOREIGN KEY (event_team_id) REFERENCES team(team_id),
    UNIQUE (event_id)
); 

CREATE TABLE IF NOT EXISTS event_clearance (
    event_id UUID,
    event_player INTEGER,
    event_position VARCHAR(100),
    event_team_id INTEGER,
    event_location_x FLOAT,
    event_location_y FLOAT,
    event_duration FLOAT,
    event_out BOOLEAN,
    event_off_camera BOOLEAN,
    event_right_foot BOOLEAN,
    event_left_foot BOOLEAN,
    event_body_part VARCHAR(100),
    event_aerial_won BOOLEAN,
    event_head BOOLEAN,
    event_other BOOLEAN,
    FOREIGN KEY (event_id) REFERENCES event(event_id),
    FOREIGN KEY (event_player) REFERENCES player(player_id),
    FOREIGN KEY (event_team_id) REFERENCES team(team_id),
    UNIQUE (event_id)
);

CREATE TABLE IF NOT EXISTS event_dispossessed (
    event_id UUID,
    event_player INTEGER,
    event_position VARCHAR(100),
    event_timestamp VARCHAR(20),
    event_team_id INTEGER,
    event_location_x FLOAT,
    event_location_y FLOAT,
    event_duration FLOAT,
    event_under_pressure BOOLEAN,
    event_off_camera BOOLEAN,
    FOREIGN KEY (event_id) REFERENCES event(event_id),
    FOREIGN KEY (event_player) REFERENCES player(player_id),
    FOREIGN KEY (event_team_id) REFERENCES team(team_id),
    UNIQUE (event_id)
);

CREATE TABLE IF NOT EXISTS event_dribble (
    event_id UUID,
    event_player INTEGER,
    event_position VARCHAR(100),
    event_location_x FLOAT,
    event_location_y FLOAT,
    event_duration FLOAT,
    event_under_pressure BOOLEAN,
    event_off_camera BOOLEAN,
    event_out BOOLEAN,
    event_outcome VARCHAR(100),
    event_overrun BOOLEAN,
    event_nutmeg BOOLEAN,
    event_no_touch BOOLEAN,
    FOREIGN KEY (event_id) REFERENCES event(event_id),
    FOREIGN KEY (event_player) REFERENCES player(player_id),
    UNIQUE (event_id)
);

CREATE TABLE IF NOT EXISTS event_dribbled_past (
    event_id UUID,
    event_player INTEGER,
    event_position VARCHAR(100),
    event_location_x FLOAT,
    event_location_y FLOAT,
    event_duration FLOAT,
    event_counterpress BOOLEAN,
    event_off_camera BOOLEAN,
    FOREIGN KEY (event_id) REFERENCES event(event_id),
    FOREIGN KEY (event_player) REFERENCES player(player_id),
    UNIQUE (event_id)
);

CREATE TABLE IF NOT EXISTS event_duel (
    event_id UUID,
    event_player INTEGER,
    event_position VARCHAR(100),
    event_team_id INTEGER,
    event_location_x FLOAT,
    event_location_y FLOAT,
    event_duration FLOAT,
    event_under_pressure BOOLEAN,
    event_outcome VARCHAR(100),
    event_type VARCHAR(100),
    event_counterpress BOOLEAN,
    event_off_camera BOOLEAN,
    FOREIGN KEY (event_id) REFERENCES event(event_id),
    FOREIGN KEY (event_player) REFERENCES player(player_id),
    FOREIGN KEY (event_team_id) REFERENCES team(team_id),
    UNIQUE (event_id)
);


-- ___________ Karan ___________  (Error to Offside)

CREATE TABLE IF NOT EXISTS event_error (
    event_id UUID,
    event_player INTEGER,
    event_position VARCHAR(100),
    event_location_x FLOAT,
    event_location_y FLOAT,
    event_duration FLOAT,
    event_under_pressure BOOLEAN,
    event_off_camera BOOLEAN,
    FOREIGN KEY (event_id) REFERENCES event(event_id),
    FOREIGN KEY (event_player) REFERENCES player(player_id),
    UNIQUE (event_id)
);

CREATE TABLE IF NOT EXISTS foul (
    event_id UUID,
    penalty BOOLEAN,
    advantage BOOLEAN,
    card_type VARCHAR(50),
    offensive BOOLEAN,
    FOREIGN KEY (event_id) REFERENCES event(event_id),
    UNIQUE (event_id)
);

CREATE TABLE IF NOT EXISTS event_foul_committed (
    event_id UUID,
    event_player INTEGER,
    event_position VARCHAR(100),
    event_location_x FLOAT,
    event_location_y FLOAT,
    event_duration FLOAT,
    event_counterpress BOOLEAN,
    off_camera BOOLEAN,
    under_pressure BOOLEAN,
    FOREIGN KEY (event_id) REFERENCES event(event_id),
    FOREIGN KEY (event_player) REFERENCES player(player_id),
    UNIQUE (event_id)
);

CREATE TABLE IF NOT EXISTS event_foul_won (
    event_id UUID,
    event_player INTEGER,
    event_position VARCHAR(100),
    event_location_x FLOAT,
    event_location_y FLOAT,
    event_duration FLOAT,
    event_under_pressure BOOLEAN,
    event_penalty BOOLEAN,
    event_defensive BOOLEAN,
    event_advantage BOOLEAN,
    off_camera BOOLEAN,
    FOREIGN KEY (event_id) REFERENCES event(event_id),
    FOREIGN KEY (event_player) REFERENCES player(player_id),
    UNIQUE (event_id)
);

CREATE TABLE IF NOT EXISTS event_goalkeeper (
    event_id UUID,
    event_player INTEGER,
    event_position VARCHAR(100),
    event_location_x FLOAT,
    event_location_y FLOAT,
    event_duration FLOAT,
    event_out BOOLEAN,
    event_under_pressure BOOLEAN,
    event_off_camera BOOLEAN,
    event_outcome VARCHAR(100),
    event_technique VARCHAR(100),
    event_body_part VARCHAR(100),
    event_shot_saved_to_post BOOLEAN,
    event_punched_out BOOLEAN,
    event_success_in_play BOOLEAN,
    event_shot_saved_off_target BOOLEAN,
    event_lost_out BOOLEAN,
    event_lost_in_play BOOLEAN,
    FOREIGN KEY (event_id) REFERENCES event(event_id),
    FOREIGN KEY (event_player) REFERENCES player(player_id),
    UNIQUE (event_id)
);

CREATE TABLE IF NOT EXISTS event_half_end (
    event_id UUID,
    event_duration FLOAT,
    event_under_pressure BOOLEAN,
    FOREIGN KEY (event_id) REFERENCES event(event_id),
    UNIQUE (event_id)
);

CREATE TABLE IF NOT EXISTS event_half_start (
    event_id UUID,
    event_duration FLOAT,
    event_under_pressure BOOLEAN,
    FOREIGN KEY (event_id) REFERENCES event(event_id),
    UNIQUE (event_id)
);

CREATE TABLE IF NOT EXISTS event_injury_stoppage (
    event_id UUID,
    event_player INTEGER,
    event_position VARCHAR(100),
    event_location_x FLOAT,
    event_location_y FLOAT,
    event_duration FLOAT,
    event_in_chain BOOLEAN,
    event_off_camera BOOLEAN,
    event_under_pressure BOOLEAN,
    FOREIGN KEY (event_id) REFERENCES event(event_id),
    FOREIGN KEY (event_player) REFERENCES player(player_id),
    UNIQUE (event_id)
);

CREATE TABLE IF NOT EXISTS event_interception (
    event_id UUID,
    event_player INTEGER,
    event_position VARCHAR(100),
    event_location_x FLOAT,
    event_location_y FLOAT,
    event_duration FLOAT,
    event_interception_outcome VARCHAR(100),
    event_counterpress BOOLEAN,
    off_camera BOOLEAN,
    under_pressure BOOLEAN,
    FOREIGN KEY (event_id) REFERENCES event(event_id),
    FOREIGN KEY (event_player) REFERENCES player(player_id),
    UNIQUE (event_id)
);

CREATE TABLE IF NOT EXISTS event_miscontrol (
    event_id UUID,
    event_player INTEGER,
    event_position VARCHAR(100),
    event_location_x FLOAT,
    event_location_y FLOAT,
    event_duration FLOAT,
    event_out BOOLEAN,
    event_under_pressure BOOLEAN,
    event_aerial_won BOOLEAN,
    event_off_camera BOOLEAN,
    FOREIGN KEY (event_id) REFERENCES event(event_id),
    FOREIGN KEY (event_player) REFERENCES player(player_id),
    UNIQUE (event_id)
);

CREATE TABLE IF NOT EXISTS event_offside (
    event_id UUID,
    event_player INTEGER,
    event_position VARCHAR(100),
    event_location_x FLOAT,
    event_location_y FLOAT,
    event_duration FLOAT,
    FOREIGN KEY (event_id) REFERENCES event(event_id),
    FOREIGN KEY (event_player) REFERENCES player(player_id),
    UNIQUE (event_id)
);


-- ___________ Arhaan ___________ (Own Goal to Tactical Shift)

CREATE TABLE IF NOT EXISTS event_own_goal_against (
    event_id UUID,
    event_player INTEGER,
    event_position VARCHAR(100),
    event_team_id INTEGER,
    event_location_x FLOAT,
    event_location_y FLOAT,
    event_duration FLOAT,
    FOREIGN KEY (event_id) REFERENCES event(event_id),
    FOREIGN KEY (event_player) REFERENCES player(player_id),
    FOREIGN KEY (event_team_id) REFERENCES team(team_id),
    UNIQUE (event_id)
);

CREATE TABLE IF NOT EXISTS event_own_goal_for (
    event_id UUID PRIMARY KEY,
    event_player INTEGER,
    event_position VARCHAR(100),
    event_team_id INTEGER,
    event_location_x FLOAT,
    event_location_y FLOAT,
    event_duration FLOAT,
    FOREIGN KEY (event_id) REFERENCES event(event_id),
    FOREIGN KEY (event_player) REFERENCES player(player_id),
    FOREIGN KEY (event_team_id) REFERENCES team(team_id),
    UNIQUE (event_id)
);


CREATE TABLE IF NOT EXISTS event_pass (
    event_id UUID,
    event_player_id INTEGER,
    event_player_name VARCHAR(100),
    event_season_id INTEGER,
    event_competition_id INTEGER,
    event_recipient_id INTEGER,
    event_recipient_name VARCHAR(100),
    event_team_id INTEGER,
    event_team_name VARCHAR(100),
    CID_SID VARCHAR(10),
    length FLOAT,
    angle FLOAT,
    height VARCHAR(100),
    end_location_x FLOAT,
    end_location_y FLOAT,
    assisted_shot VARCHAR(100),
    backheel BOOLEAN,
    deflected BOOLEAN,
    miscommunication BOOLEAN,
    is_cross BOOLEAN,
    cutback BOOLEAN,
    switch BOOLEAN,
    shot_assist BOOLEAN,
    goal_assist BOOLEAN,
    body_part VARCHAR(100),
    type VARCHAR(100),
    outcome VARCHAR(100),
    technique VARCHAR(100),
    FOREIGN KEY (event_id) REFERENCES event(event_id),
    FOREIGN KEY (event_player_id) REFERENCES player(player_id),
    FOREIGN KEY (event_season_id) REFERENCES season(season_id),
    FOREIGN KEY (event_competition_id) REFERENCES competition(competition_id),
    FOREIGN KEY (event_recipient_id) REFERENCES player(player_id),
    UNIQUE (event_id)
);

CREATE TABLE IF NOT EXISTS event_playerOff (
    event_id UUID,
    event_player INTEGER,
    event_position VARCHAR(100),
    event_location_x FLOAT,
    event_location_y FLOAT,
    event_duration FLOAT,
    event_off_camera BOOLEAN,
    FOREIGN KEY (event_id) REFERENCES event(event_id),
    FOREIGN KEY (event_player) REFERENCES player(player_id),
    UNIQUE (event_id)
);

CREATE TABLE IF NOT EXISTS event_playerOn (
    event_id UUID,
    event_player INTEGER,
    event_position VARCHAR(100),
    event_location_x FLOAT,
    event_location_y FLOAT,
    event_duration FLOAT,
    event_off_camera BOOLEAN,
    FOREIGN KEY (event_id) REFERENCES event(event_id),
    FOREIGN KEY (event_player) REFERENCES player(player_id),
    UNIQUE (event_id)
);

CREATE TABLE IF NOT EXISTS event_pressure(
    event_id UUID,
    event_player INTEGER,
    event_position VARCHAR(100),
    event_location_x FLOAT,
    event_location_y FLOAT,
    event_duration FLOAT,
    event_counterpress BOOLEAN, 
    event_under_pressure BOOLEAN,
    event_off_camera BOOLEAN,
    FOREIGN KEY (event_id) REFERENCES event(event_id),
    FOREIGN KEY (event_player) REFERENCES player(player_id),
    UNIQUE (event_id)
);

CREATE TABLE IF NOT EXISTS event_refereeBallDrop (
    event_id UUID,
    event_duration FLOAT,
    event_location_x FLOAT,
    event_location_y FLOAT,
    event_off_camera BOOLEAN,
    FOREIGN KEY (event_id) REFERENCES event(event_id),
    UNIQUE (event_id)
);

CREATE TABLE IF NOT EXISTS event_shield (
    event_id UUID,
    event_player INTEGER,
    event_position VARCHAR(100),
    event_possession_team_id INTEGER,
    event_location_x FLOAT,
    event_location_y FLOAT,
    event_duration FLOAT,
    event_under_pressure BOOLEAN,
    FOREIGN KEY (event_id) REFERENCES event(event_id),
    FOREIGN KEY (event_player) REFERENCES player(player_id),
    FOREIGN KEY (event_possession_team_id) REFERENCES team(team_id),
    UNIQUE (event_id)
);

CREATE TABLE IF NOT EXISTS freeze_frame (
    freeze_frame_id SERIAL PRIMARY KEY,
    event_id UUID,
    event_player INTEGER,
    event_location_x FLOAT,
    event_location_y FLOAT,
    event_position VARCHAR(100),
    event_teammate BOOLEAN,
    FOREIGN KEY (event_id) REFERENCES event(event_id),
    FOREIGN KEY (event_player) REFERENCES player(player_id),
    UNIQUE (event_id)
);

CREATE TABLE IF NOT EXISTS event_shot (
    event_id UUID,
    event_player_id INTEGER,
    event_player_name VARCHAR(100),
    event_season_id INTEGER,
    event_competition_id INTEGER,
    event_position VARCHAR(100),
    event_team_id INTEGER,
    event_team_name VARCHAR(100),
    event_location_x FLOAT,
    event_location_y FLOAT,
    event_duration FLOAT,
    event_out BOOLEAN,
    event_under_pressure BOOLEAN,
    event_off_camera BOOLEAN,
    event_statsbomb_xg FLOAT,
    end_location_x FLOAT,
    end_location_y FLOAT,
    event_body_part VARCHAR(100),
    event_outcome VARCHAR(100),
    event_first_time BOOLEAN,
    event_technique VARCHAR(100),
    event_deflected BOOLEAN,
    event_one_on_one BOOLEAN,
    event_aerial_won BOOLEAN,
    event_saved_to_post BOOLEAN,
    event_redirect BOOLEAN,
    event_open_goal BOOLEAN,
    event_follows_dribble BOOLEAN,
    event_saved_off_target BOOLEAN,
    event_freeze_frame_id INTEGER,
    FOREIGN KEY (event_id) REFERENCES event(event_id),
    FOREIGN KEY (event_season_id) REFERENCES season(season_id),
    FOREIGN KEY (event_competition_id) REFERENCES competition(competition_id),
    FOREIGN KEY (event_team_id) REFERENCES team(team_id),
    FOREIGN KEY (event_team_id) REFERENCES team(team_id),
    FOREIGN KEY (event_freeze_frame_id) REFERENCES freeze_frame(freeze_frame_id),
    UNIQUE (event_id)   
);

--not sure about this about line up
CREATE TABLE IF NOT EXISTS event_startingXI (
    event_id UUID,
    event_player INTEGER,
    event_position VARCHAR(100),
    event_location_x FLOAT,
    event_location_y FLOAT,
    event_formations INTEGER,
    event_lineup INTEGER,
    event_jersey_number INTEGER,
    FOREIGN KEY (event_id) REFERENCES event(event_id),
    FOREIGN KEY (event_player) REFERENCES player(player_id),
    UNIQUE (event_id)
);

CREATE TABLE IF NOT EXISTS event_substitution (
    event_id UUID,
    event_player_out INTEGER,
    event_player_replacement INTEGER,
    event_timestamp VARCHAR(20),
    event_duration FLOAT,
    FOREIGN KEY (event_id) REFERENCES event(event_id),
    FOREIGN KEY (event_player_out) REFERENCES player(player_id),
    FOREIGN KEY (event_player_replacement) REFERENCES player(player_id),
    UNIQUE (event_id)
);

CREATE TABLE IF NOT EXISTS event_tactical_shift (
    event_id UUID,
    event_duration FLOAT,
    event_timestamp VARCHAR(20),
    event_formations INTEGER,
    event_lineup INTEGER,
    FOREIGN KEY (event_id) REFERENCES event(event_id),
    UNIQUE (event_id)
);


-- INDEXES
CREATE INDEX idx_event_shot_season_id ON event_shot USING btree(event_season_id, event_competition_id);
-- CREATE INDEX IF NOT EXISTS idx_event_shot_season_id_hash ON event_shot USING hash(event_season_id);
-- CREATE INDEX idx_event_pass_CID ON event_pass USING hash(CID_SID);
CREATE INDEX idx_event_pass_SID_CID ON event_pass USING btree(event_season_id, event_competition_id);
