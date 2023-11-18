## data
- Die hier zu findene Datei enthält Daten zu den Ergebnissen von Fifa Word Cup Spielen seit 1930. 
- Die Datei hat folgende Spalten 
   - HomeTeam: Land bzw. Manschaft, die das Spiel ausgerichtet hat
   - AwayTeam: Land bzw. Manschaft, die als Gast angereist ist
   - Year: Jahr in dem das Spiel stattgefunden hat
   - HomeGoals: Anzahl an Toren, die das HomeTeam geschossen hat
   - AwayGoals: Anzahl an Toren, die das AwayTeam geschossen hat
   - TotalGoals: Anzahl an Toren, die insgesamt in einem Spiel gefallen sind 

## src
- Dieser Ordner enthält den Python Code, mit welchem die Analyse durchgeführt werden kann
   ## main.py
   - Dieses File stellt den Einstiegspunkt für das Programm dar, da es die Methode main() enthält. 
   - Die Main Methode lädt die Analysefunktion aus dem Submodul analysis.fifa_analysis und startet diese. 

   ## analysis.fifa_analysis
   - Dies ist ein Submodul, in welchem die Auswertung der Fifaworldcup Daten mit Hilfe von Pyspark durchgeführt werden. 
   - Das File fifa_analysis.py enthält eine Methode fifa_spark_analysis,. welche wiederrum eine Submethode process_line verwendet

      ## fifa_spark_analysis
      1. Initialisierung einer Spark Session
      2. Laden der Daten aus dem clean_fifa_worldcup_matches File und mappen der Daten mit Hilfe der process_line Submethode
      3. Reduzieruzng der Daten durch eine Aggregartion / Gruppierung nach zurückgegebenen Team
      4. Filtern der Daten, um alle Unentschieden zu entfernen
      5. Sortieren der Daten 
      6. Konvertierung in eine Liste
      7. Liste in Dataframe umwandeln 
      8. Schreiben der Ergebnisse in die Datei part-00000-....csv im Ordner results
      9. Zusätzliche Ausgabe der Ergebnisse in der Konsole
      10. Beenden der Spark Session

      ## process_line
      - Diese Submethode verarbeitet jeweils eine Zeile der CSV Datei
      1. Aufspalten der Zeile in die einzelnen Felder
      2. Abfrage, welches Team gewonnen hat (bzw. ob es ein unentschieden gab), indem Toranzahl verglichen wird
      3. Zurückgabe des Ergebnisses als Tupel

## results
- Die hier zufindene CSV Datei (part-0000....csv) enthält die Ergebnisse der Analyse. 
- Die Datei besteht aus 2 Spalten: 
   - Team: Namen des Teams
   - Anzahl Win: Anzahl an Spielen, die das Team gewonnen hat
- Die Einträge sind absteigend nach Anzahl der Siege sortiert

