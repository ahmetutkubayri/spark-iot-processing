# Solutions to IoT Temperature Processing

This file contains solutions to the given IoT data processing tasks.

## Q-1: Generate Data in Kafka
```bash
docker exec -it kafka mkdir -p /tmp/iot-temp-input
```

## Q-2: Copy Dataset to Spark Container
```bash
docker cp IOT-temp.csv kafka:/tmp/iot-temp-input
```

## Q-3: Spark Streaming Application
```python
from pyspark.sql import SparkSession, functions as F
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

spark = SparkSession.builder     .appName("IoT Temperature Processing")     .getOrCreate()

spark.sparkContext.setLogLevel("ERROR")

input_path = "/tmp/iot-temp-input/"
output_path = "/tmp/iot-temp-output/"
checkpointDir = "/tmp/iot-temp-checkpoint"

schema = StructType([
    StructField("id", StringType(), True),
    StructField("room_id/id", StringType(), True),
    StructField("noted_date", StringType(), True),
    StructField("temp", IntegerType(), True),
    StructField("out/in", StringType(), True)
])

df = spark.readStream.format("csv")     .option("header", True)     .schema(schema)     .option("sep", ",")     .load(input_path)

iot_df = df     .withColumn("Date", F.to_date(F.col("noted_date"), "MM-dd-yyyy HH:mm"))     .withColumn("Year", F.year(F.col("Date")))     .withColumn("Month", F.month(F.col("Date")))     .withColumn("Day_of_Week", F.dayofweek(F.col("Date")))

output = iot_df.writeStream     .outputMode("append")     .format("csv")     .option("header", True)     .option("checkpointLocation", checkpointDir)     .option("path", output_path)     .start()

output.awaitTermination()
```

This script processes IoT temperature data by adding `Year`, `Month`, and `Day of the Week`, then writes it to `/tmp/iot-temp-output/`.
