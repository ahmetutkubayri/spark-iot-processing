# Environment Setup Guide

This document provides a step-by-step guide to setting up the Spark Streaming environment.

## Step 1: Install Required Libraries
```bash
pip install pyspark
```

## Step 2: Start Docker Environment
```bash
docker-compose up -d
```

## Step 3: Download and Extract Dataset
```bash
wget https://github.com/erkansirin78/datasets/raw/master/IOT-temp.csv.zip
unzip IOT-temp.csv.zip
```

## Step 4: Run the Spark Streaming Script
```bash
docker exec -it spark bash
spark-submit iot_temp_processing.py
```

## Step 5: Verify Output Data
Check the processed data:
```bash
ls /tmp/iot-temp-output/
```

