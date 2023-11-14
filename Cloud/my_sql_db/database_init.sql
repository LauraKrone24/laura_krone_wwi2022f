
CREATE TABLE artists(
    artistID int not null AUTO_INCREMENT, 
    artist_name varchar(100) not null, 
    times_played int not null DEFAULT 0, 
    primary Key(artistID)
);


INSERT INTO artists(artist_name,times_played)
VALUES ("Katy Perry", 1000), ("Ed Sheeran", 1500), ("NEFFEX",20), ("Nickelback",900);



