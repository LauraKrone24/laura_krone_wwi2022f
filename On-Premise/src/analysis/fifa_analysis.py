
from pyspark.sql import SparkSession 

'''
    In dieser Methode wird die Analyse der Fifa Daten durchgeführt und abgespeichert.
    Fragestellung der Analse lautet: 
         Welche Ländern haben am häufigsten gewonnen?

'''

def fifa_spark_analysis(): 

    # Initialisieren der Spark Session
    spark = SparkSession \
       .builder \
       .appName("CountWins") \
       .getOrCreate()


    # Submethode, welche einen einzelne Zeile der Orginal CSV Datei verarbeitet und den Gewinner zurückgibt
    def process_line(line):
        fields=line.split(",")
        if(fields[3]>fields[4] ):
            return fields[0],1
        elif(fields[4]>fields[3]):
            return fields[1],1
        else: 
           return "Unentschieden", 1

        
    # Laden, Mappen, Reducen, Filtern und Soritieren der Daten
    result_list =spark.sparkContext.textFile("./On-Premise/data/clean_fifa_worldcup_matches.csv")\
        .map(process_line)\
        .reduceByKey(lambda x,y : x + y)\
        .filter(lambda x: x[0]!="Unentschieden")\
        .sortBy(lambda x: x[1], False)\
        .collect()
    
    #Wandeln des der Result Liste in einen Spark DataFrame
    results = spark.createDataFrame(result_list,schema=["Team", "Anzahl Win"])

    #Schreiben der Ergebnisse in eine CSV Datei
    results.coalesce(1)\
       .write\
       .mode("overwrite")\
       .format("com.databricks.spark.csv")\
       .option("header", "true")\
       .save("On-Premise/results")


    #Ausgabe der Ergebnisse in der Konsole 
    results.show()  
    top_team =results.collect()[0]
    print("Mit ",top_team[1]," Siegen ist ",top_team[0]," das erfolgreichste Team!!")
    
    # Stoppen der Spark Session
    spark.stop()