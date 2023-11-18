## DOCKER-COMPOSE.YML
- Dieses File dient dazu beide Container hochzufahren. Es enthält: 
    - Die Konfigurationen für die Container, für die Datenbank und den Mikroservice
        - Hier werden u.a. die Kontainernamen, Ports und Netzwerkzugehörigkeit vergeben 
    - Es wird zudem auch ein Netzwerk angelegt, dem beiden Conatiner angehören, welches den Namen "big_data_abgabe_wi22001" hat

## .env
- Dieses File enthält alle für die verschiedenen Services benötigten Variablen wie u.a. Datenbankname und Passwort

## MY SQL DB 
- In diesen Ordner befinden sich alles Nötwendige zum dockerisieren der Datenbank

    # Dockerfile
    - Dieses File wird genutzt, um das Image für die MySQL Datenbank zu bauen. 
    - Das Image basiert auf dem neusten My SQL Image 
    - Es wird die Datei database_init.sql an den Startpunkt des Conatainers kopiert 

    # database_init.sql
    - Dieses File enthält die Funktionen, um eine Beispieldatenbank zu initialieren, wenn keine persistent gespeicherten Daten vorhanden sind
    - Zuerst wird die Datenbank zu my_database gewechselt
    - Dann wird die Tabelle Artist, welche eine ID, einen Künstlernamen und eine Anzahl an Aufrufen enthält erstellt, falls sie noch nicht vorhanden ist 
    - Dann wird diese Tabelle, falls sie leer ist mit Beispieldaten gefüllt

## MY MICOR SERVICE
- In diesen Ordner befinden sich alles Nötwendige zum dockerisieren des Micorservices, welcher die sortierten Daten der Tabelle artists aus dem Datenbankcontainer zurückgibt

    # requirements.txt
    - Dieses File enthält die benötigten Anforderungen, die für den Microservice im Container installiert werden müssen 

    # Dockerfile
    - Dieses File wird genutzt, um das Image für den Python Microservice zu bauen. 
    - Das Image basiert auf dem neusten Python Image 
    - Es werden alle benötigten Anforderungen installiert und der Microservice wird mit Python auf Localhost gestartet

    # app.py
    - Dieses File enthält die Python Anwendung für den Microservice. Sie besteht aus 2 Methoden: 
    1. Eine Main Methode, welche den Startpunkt für das Programm bildet
    2. Eine show_artists Methode, die über localhost:3000/artists aufrufbar ist. In ihr wird eine Verbindung zur MySql Datenbank hergestellt und die nach aufrufen absteigend sortierten Künstler werden zurückgegeben 

    

