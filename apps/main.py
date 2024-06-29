from pyspark.sql import SparkSession


# Configura la sesión de Spark
spark = SparkSession.builder \
    .appName("PostgreSQLExample") \
    .getOrCreate()


# Configura las opciones de conexión a PostgreSQL
jdbc_url = "jdbc:postgresql://demo-database:5432/my_database"
db_properties = {
    "user": "postgres",
    "password": "1234",
    "driver": "org.postgresql.Driver"
}


# Lee datos de PostgreSQL
df = spark.read.jdbc(url=jdbc_url, table="my_table", properties=db_properties)


# Realiza algunas transformaciones básicas
df = df.filter(df["some_column"] > 0)  # Filtra filas donde 'some_column' es mayor que 0
df = df.select("column1", "column2")   # Selecciona las columnas 'column1' y 'column2'


# Muestra las primeras 10 filas del DataFrame
df.show(10)


# Guarda el resultado en formato Parquet
df.write.parquet("/opt/spark-data/output/my_table")


# Finaliza la sesión de Spark
spark.stop()
