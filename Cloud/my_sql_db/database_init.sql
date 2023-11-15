
-- Nutzung der richtigen Datenbank
USE my_database

-- Erzeugen einer Tabelle, wenn sie noch nicht existiert
CREATE TABLE IF NOT EXISTS artists (
    artist_ID int not null AUTO_INCREMENT, 
    artist_name varchar(100) not null, 
    times_played int not null DEFAULT 0, 
    primary Key(artist_ID)
);

-- Eintragen von Beispielwerten, wenn die Tabelle leer ist 
INSERT INTO artists (artist_name, times_played)
SELECT * FROM(
    VALUES
    ROW( "Katy Perry", 1000),
    ROW( "Ed Sheeran", 1500),
    ROW("NEFFEX",20),
    ROW( "Nickelback",900)
) source_data
WHERE  (SELECT COUNT(*) FROM artists) =0;









