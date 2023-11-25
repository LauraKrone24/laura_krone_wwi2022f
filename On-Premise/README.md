# Big Data Programming - Teil 1: On Premise

Die Analyse, die hier durchgeführt werden, sind Teil der benoteten Abgabe für das Modul Big Data. 
Sie befassen sich mit Pyspark. 

Abgabetermin: 26.11.2023
Dozent: Bernhard Ortner

Kurs: WWI2022F
Name: Laura Krone
Email: wi22001@lehre.dhbw-stuttgart.de
Matrikelnr.: 1130769

## Dokumentation
- Dokumentation zu den in diesem Projekt verwendeten Methoden befindet sich in /doc/README.md

## Ausführung
- Entpacke die Zip-Datei in einen Ordner einen gleichnamigen Ordner 
- Die Analyse kann in VSCode in dem durch die Datei main.py, welche sich in dem Ordner /src befindet gestartet werden 
- Ausführen im Terminal
    - Navigation in den Ordner /src
    - Ausführen des Befehls "python main.py" bzw "python3 main.py"

## Datengrundlage
- Es werden die in der Aufgabenstellung vorgeschlagenen Fifadaten verwendet
- Die Daten enthalten die Spielergebnisse aller Fifa Worldcup Matches seit 1930
- Online zu finden sind die Daten unter: https://raw.githubusercontent.com/ifrankandrade/fifa-world-cup-2022-prediction/main/data/clean_fifa_worldcup_matches.csv
- Innerhalb dieses Projektes befinden sich die Daten unter data/clean_fifa_worldcup_matches.csv

## Umsetzung
- In "setup.py" und "setup.cfg" sind alle technische Voraussetzungen und Dependencies definiert
- Genauere Erläuterungen befinden sich im Programmcode der Analyse (src\main.py)

## Ergebnisse
- Ergenisse der Analyse werden zum einen teilweise in der Konsole ausgegeben
- zusätzlich werden die Ergebnisse in eine CSV Datei gespeichert (results\part-00000-....csv)


