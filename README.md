# IoT Temperature Data Processing with Spark Streaming

This project processes IoT temperature data in real-time using Apache Spark. It reads temperature logs from Kafka, performs transformations, and writes results to local storage.

## 🚀 Features
- Read streaming IoT data from Kafka
- Transform data (adding Year, Month, and Day of the week columns)
- Store results in CSV format
- Uses `00_spark_kafka_postgres_minio_docker_compose` environment

## 📁 Repository Structure
- `iot_temp_processing.py` → Python script for Spark streaming processing
- `setup.md` → Guide for setting up Spark, Kafka, and PostgreSQL
- `solutions.md` → Explanation of transformations and processing steps

## 🔧 Prerequisites
- Docker setup with Kafka and Spark
- Dataset from:
  ```
  https://github.com/erkansirin78/datasets/raw/master/IOT-temp.csv.zip
  ```

## 🏗️ Running the Processing Script
1. Start the environment:
   ```bash
   docker-compose up -d
   ```

2. Copy dataset to Kafka:
   ```bash
   docker exec -it kafka mkdir -p /tmp/iot-temp-input
   docker cp IOT-temp.csv kafka:/tmp/iot-temp-input
   ```

3. Run Spark streaming:
   ```bash
   docker exec -it spark bash
   spark-submit iot_temp_processing.py
   ```

4. Processed data will be saved in `/tmp/iot-temp-output/`.
