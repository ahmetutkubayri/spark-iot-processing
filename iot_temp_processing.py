from pyspark.sql import SparkSession, functions as F
from pyspark.sql.types import StructType, StructField, StringType, IntegerType


spark = SparkSession.builder \
    .appName("IoT Temperature Processing") \
    .getOrCreate()

input_path = "/tmp/iot-temp-input/"
output_path = "/tmp/iot-temp-output/"

tmp_df = spark.read.format("csv") \
    .option("header", True) \
    .option("sep", ",") \
    .option("inferSchema", True) \
    .load(input_path)

tmp_df.limit(5).toPandas()

schema = StructType([
    StructField("id", StringType(), True),
    StructField("room_id/id", StringType(), True),
    StructField("noted_date", StringType(), True),
    StructField("temp", IntegerType(), True),
    StructField("out/in", StringType(), True)
])

df = spark.readStream.format("csv") \
.option("header", True) \
.schema(schema) \
.option("sep", ",") \
.load(input_path)




iot_df = df \
.withColumn("Date", F.to_date(F.col("noted_date"), "MM-dd-yyyy HH:mm")) \
.withColumn("Year", F.year(F.col("Date"))) \
.withColumn("Month", F.month(F.col("Date"))) \
.withColumn("Day_of_Week", F.dayofweek(F.col("Date")))

output = iot_df.writeStream \
    .outputMode("append") \
    .format("csv") \
    .option("header", True) \
    .option("checkpointLocation", "/tmp/iot-temp-checkpoint") \
    .option("path", output_path) \
    .start()
    


output.awaitTermination()

homework = spark.read.format("csv") \
    .option("header", True) \
    .option("sep", ",") \
    .load(output_path)

homework.limit(5).toPandas()

