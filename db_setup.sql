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

CREATE TABLE IF NOT EXISTS season_match (
    season_id INTEGER, -- Foreign Key
    match_id INTEGER PRIMARY KEY,
    FOREIGN KEY (season_id) REFERENCES season(season_id),
    FOREIGN KEY (match_id) REFERENCES match(match_id),
    UNIQUE (season_id, match_id)
);

CREATE TABLE IF NOT EXISTS team_manager (
    team_id INTEGER, -- Foreign Key
    manager_id INTEGER, -- Foreign Key
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

-- Create Lineup table
CREATE TABLE IF NOT EXISTS lineup (
    match_id INTEGER,
    team_id INTEGER,
    player_id INTEGER,
    FOREIGN KEY (match_id) REFERENCES match(match_id),
    FOREIGN KEY (team_id) REFERENCES team(team_id),
    FOREIGN KEY (player_id) REFERENCES player(player_id),
    UNIQUE (match_id, team_id, player_id)
);

-- Create Position table
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

-- Create Card table
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

-- SELECT * FROM card;
-- SELECT * FROM competition;
-- SELECT * FROM competition_season;
-- SELECT * FROM lineup;
-- SELECT * FROM manager;
-- SELECT * FROM match;
-- SELECT * FROM player;
-- SELECT * FROM position;
-- SELECT * FROM referee;
-- SELECT * FROM season;
-- SELECT * FROM season_match;
-- SELECT * FROM stadium;
-- SELECT * FROM team;
-- SELECT * FROM team_manager;
