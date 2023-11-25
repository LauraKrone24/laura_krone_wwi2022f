# Big Data Programming - Teil 2: Cloud

Die Datenbank und der Microservice, welche hier dockerisiert werden, sind Teil der benoteten Abgabe für das Modul Big Data. 
Die Datenbank enthält zu Beginn 4 Künstler und eine fiktive Anzahl an Aufrufen. Der Mikroservice fragt diese Datenbank ab und gibt die Künstler sortiert nach Anzahl ihrer Aufrufe aus. 

Abgabetermin: 26.11.2023
Dozent: Bernhard Ortner

Kurs: WWI2022F
Name: Laura Krone
Email: wi22001@lehre.dhbw-stuttgart.de
Matrikelnr.: 1130769

## Dokumentation
- Dokumentation zu den in diesem Projekt verwendeten Methoden und Files befindet sich in /doc/README.md

## Starten der Container 
0. Falls noch nicht vorhanden Docker und docker-compose installieren und verfügbar machen
1. Im Terminal in den Ornder /Cloud navigieren
2. Eingabe des Befehls "docker-compose up"

## Zugriff auf die Datenbank
- Eine Bearbeitung der Datenbank ist im Container selbst möglich. Dazu müssen folgende Schritte ausgeführt werden: 
1. Starten der Container durch "docker-compose up"
2. Anzeigen der laufenden Container durch "docker container ls"
3. Kopieren der Container ID des Containers mit dem Namen my_sql_database
4. Aufschalten auf den Container mit "docker exec -it ContainerID /bin/bash"
5. Zugreifen auf die Datenbank mit "mysql -proot"
6. Wechseln zu richtigen Datenbank mit "use my_database"
7. An dieser Stelle kann nun SQL Code genutzt werden, um die Datenbank zu betrachten bzw. zu verändern

## Zugriff auf den Microservice
- Wenn beide Container gestartet sind, muss der Befehl "curl localhost:3000/artists" ausgeführt werden, um auf den Microservice zuzugreifen 
- Alternativ kann man die Rückmeldungen des Microservice auch unter http://localhost:3000/artists ansehen


## Alternatives Startes durch docker build und docker run
- Falls im Rahmen der Aufgabenüberprüfung beide Conatiner einzeln über den docker run Befehl ausgeführt werden sollen, können folgende Befehle verwendet werden, um alle notwendig Parameter zu setzen: 

    ## Netzwerk 
    1. Führe den Befehl "docker network create big_data_abgabe_wi22001"

    ## my_sql_db
    1. Navigiere in den Ordner my_sql_db
    2. Führe den Befehl "docker build -t my_sql_image ." aus, um das Image zu bauen
    3. Führe den Befehl "docker run --name my_sql_database -v /Users/laura/wi22001/mysql_db/mysql:/var/lib/mysql -v /Users/laura/wi22001/mysql_db/logs:/var/log -p 3306:3306 --env-file ../.env --network big_data_abgabe_wi22001 my_sql_image"

    ## my_sql_db
    1. Navigiere in den Ordner my_micro_service
    2. Führe den Befehl "docker build -t my_service_image ." aus, um das Image zu bauen
    3. Führe den Befehl "docker run -v /Users/laura/wi22001/my_micro_service/logs:/var/log -p 3000:3000 --env-file ../.env --network big_data_abgabe_wi22001 my_service_image"