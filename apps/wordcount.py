# wordcount.py
from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession

# Create a SparkSession
spark = SparkSession.builder \
    .appName("WordCount") \
    .getOrCreate()

# Read the input file
input_file = "hdfs://lorem-ipsum.txt"
text_file = spark.read.text(input_file).rdd.map(lambda r: r[0])

# Split the lines into words
words = text_file.flatMap(lambda line: line.split(" "))

# Count each word
word_counts = words.map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)

# Save the counts to an output file
output_path = "hdfs://./output"  # Actualiza esta ruta con la ruta correcta a tu carpeta de salida
word_counts.saveAsTextFile(output_path)

spark.stop()
