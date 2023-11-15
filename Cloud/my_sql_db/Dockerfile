#Laden des aktuellsten MySQL Images 
FROM mysql:latest

#Kopieren des Datenbank Init Files zum Startpunkt des Containers 
COPY ./database_init.sql ./docker-entrypoint-initdb.d/
