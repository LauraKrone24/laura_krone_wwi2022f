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
0. Falls noch nicht vorhanden Docker und docker-compose installieren
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

