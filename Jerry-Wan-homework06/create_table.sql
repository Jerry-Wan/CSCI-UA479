-- write your table creation sql here!
CREATE DATABASE homework06;
\c homework06

CREATE TABLE esport(
    game_name varchar(100) PRIMARY KEY,
    release_date numeric NOT NULL,
    genre varchar(50) NOT NULL,
    total_earning numeric NOT NULL,
    total_player numeric NOT NULL,
    total_tournament numeric NOT NULL
);

