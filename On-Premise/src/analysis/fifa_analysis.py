
from pyspark.sql import SparkSession 

'''
    In dieser Methode wird die Analyse der Fifa Daten durchgeführt und abgespeichert.
    Fragestellung der Analse lautet: 
         Wie häufig haben die verschiedenen Länder gewonnen und wie oft gab es insgesamt ein unentschieden?

'''

def fifa_spark_analysis():  
    spark = SparkSession \
       .builder \
       .appName("CountWins") \
       .getOrCreate()



    def process_line(line):
        fields=line.split(",")
        if(fields[3]>fields[4] ):
            return fields[0],1
        elif(fields[4]>fields[3]):
            return fields[1],1
        else: 
           return "Unentschieden", 1

        
        

  
    mapping =spark.sparkContext.textFile("./On-Premise/data/clean_fifa_worldcup_matches.csv")\
        .map(process_line)\
        .reduceByKey(lambda x,y : x + y)\
        .sortBy(lambda x: x[1], False)\
        .collect()
    

    results = spark.createDataFrame(mapping,schema=["Team", "Anzahl Win"])

    results.coalesce(1)\
       .write\
       .mode("overwrite")\
       .format("com.databricks.spark.csv")\
       .option("header", "true")\
       .save("On-Premise/results")



    results.show()  
    

  
    spark.stop()