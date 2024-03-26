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
    competition_id INTEGER, -- Foreign Key
    season_id INTEGER, -- Foreign Key
    FOREIGN KEY (competition_id) REFERENCES competition(competition_id),
    FOREIGN KEY (season_id) REFERENCES season(season_id)
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

CREATE TABLE IF NOT EXISTS matches (
    match_id INTEGER PRIMARY KEY,
    match_date DATE,
    kick_off TIME,
    stadium_id INTEGER, -- Foreign Key
    referee_id INTEGER, -- Foreign Key
    home_team_id INTEGER, -- Foreign Key
    away_team_id INTEGER, -- Foreign Key
    home_score INTEGER,
    away_score INTEGER,
    match_status VARCHAR(100),
    match_week INTEGER,
    competition_stage VARCHAR(100),
    FOREIGN KEY (stadium_id) REFERENCES stadium(stadium_id),
    FOREIGN KEY (referee_id) REFERENCES referee(referee_id),
    FOREIGN KEY (home_team_id) REFERENCES team(team_id),
    FOREIGN KEY (away_team_id) REFERENCES team(team_id)
);

CREATE TABLE IF NOT EXISTS season_matches (
    season_id INTEGER, -- Foreign Key
    match_id INTEGER PRIMARY KEY,
    FOREIGN KEY (season_id) REFERENCES season(season_id),
    FOREIGN KEY (match_id) REFERENCES matches(match_id)
);

CREATE TABLE IF NOT EXISTS team_manager (
    team_id INTEGER, -- Foreign Key
    manager_id INTEGER, -- Foreign Key
    FOREIGN KEY (team_id) REFERENCES team(team_id),
    FOREIGN KEY (manager_id) REFERENCES manager(manager_id)
);

CREATE TABLE IF NOT EXISTS position (
    position_id INTEGER PRIMARY KEY,
    position VARCHAR(100),
    from_time TIME,
    to_time TIME,
    from_period INTEGER,
    to_period INTEGER,
    start_reason VARCHAR(100),
    end_reason VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS card (
    card_id INTEGER PRIMARY KEY,
    card_time TIME,
    card_type VARCHAR(100),
    card_reason VARCHAR(100),
    card_period INTEGER
);

CREATE TABLE IF NOT EXISTS player (
    player_id INTEGER PRIMARY KEY,
    player_name VARCHAR(100),
    player_nickname VARCHAR(100),
    jersey_number INTEGER,
    country_name VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS lineup (
    lineup_id INTEGER PRIMARY KEY,
    player_id INTEGER, 
    card_id INTEGER,
    position_id INTEGER,
    FOREIGN KEY (player_id) REFERENCES player(player_id),
    FOREIGN KEY (position_id) REFERENCES position(position_id),
    FOREIGN KEY (card_id) REFERENCES card(card_id)
);

CREATE TABLE IF NOT EXISTS team_lineup (
    team_id INTEGER, -- Foreign Key
    lineup_id INTEGER PRIMARY KEY,
    FOREIGN KEY (team_id) REFERENCES team(team_id),
    FOREIGN KEY (lineup_id) REFERENCES lineup(lineup_id)
);

-- Drop the tables
-- DROP TABLE IF EXISTS team_lineup;
-- DROP TABLE IF EXISTS lineup;
-- DROP TABLE IF EXISTS player;
-- DROP TABLE IF EXISTS card;
-- DROP TABLE IF EXISTS position;
-- DROP TABLE IF EXISTS team_manager;
-- DROP TABLE IF EXISTS matches;
-- DROP TABLE IF EXISTS season_matches;
-- DROP TABLE IF EXISTS team;
-- DROP TABLE IF EXISTS stadium;
-- DROP TABLE IF EXISTS referee;
-- DROP TABLE IF EXISTS competition;
-- DROP TABLE IF EXISTS manager;
-- DROP TABLE IF EXISTS season;


-- SELECT * FROM manager;
-- SELECT * FROM referee;
-- SELECT * FROM competition;
-- SELECT * FROM season;
-- SELECT * FROM stadium;
-- SELECT * FROM team;
-- SELECT * FROM matches;
-- SELECT * FROM team_manager;
-- SELECT * FROM position;
-- SELECT * FROM card;
-- SELECT * FROM player;
-- SELECT * FROM lineup;
-- SELECT * FROM team_lineup;
