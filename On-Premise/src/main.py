'''
    Autor: Laura Krone
    Version: 1
    Beschreibung:   Startpunkt für ein Programm,
                    welches mit Spark die Anzahl an Siegen von Ländern in Fifa World Cup Spielen berechnet,
                    die Manschaften nach ihrer Sieganzahl soritiert und 
                    die Ergebnisse abspeichert
'''


def main():
    from analysis.fifa_analysis import fifa_spark_analysis as start_analysis
    start_analysis()



if __name__ == "__main__":
    main()
