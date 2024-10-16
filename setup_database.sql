CREATE DATABASE baseball;

\connect baseball;

CREATE TABLE processed_statcast (
    game_date DATE,
    player_name VARCHAR(50),
    launch_speed DECIMAL,
    launch_angle DECIMAL,
    hit_distance DECIMAL,
    hit_type VARCHAR(20),
    player_team VARCHAR(50)
);
