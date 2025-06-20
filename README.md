# Real-Time User Data Streaming Pipeline

A fully containerized, real-time data pipeline for ingesting, processing, and storing user data from the [Random User API](https://randomuser.me). Built using Apache Kafka, Apache Spark Streaming, Apache Cassandra, and orchestrated via Apache Airflow—all running inside Docker.

---

## 🚀 Overview

This project demonstrates a complete real-time data engineering workflow:

1. **Data Ingestion** – Python scripts fetch synthetic user data from Random User API and push it to Kafka topics.
2. **Streaming Processing** – Apache Spark consumes and processes these events from Kafka in real-time.
3. **Storage** – Cleaned and transformed data is written into Apache Cassandra for durable storage and querying.
4. **Orchestration** – Apache Airflow schedules and manages the end-to-end workflow.

---

## 🧱 Tech Stack

| Layer        | Technology                |
|--------------|---------------------------|
| Ingestion     | Python, Random User API   |
| Messaging     | Apache Kafka, Apache Zookeeper |
| Processing    | Apache Spark Streaming     |
| Storage       | Apache Cassandra           |
| Orchestration | Apache Airflow             |
| Containerization | Docker, Docker Compose |

---

## 🔄 Data Flow Architecture

1. `Python Producer`: Fetches random user profiles every N seconds and sends JSON data to a Kafka topic (`user_topic`).
2. `Kafka`: Buffers and brokers real-time user data to consumers.
3. `Spark Streaming`: Subscribes to the Kafka topic, transforms and cleans data.
4. `Cassandra Sink`: Stores the transformed user data for querying.
5. `Airflow DAG`: Controls the start/stop of pipeline components and manages retries and dependencies.

---

## 📂 Project Structure

```bash
.
├── docker-compose.yml
├── airflow/
│   └── dags/streaming_pipeline.py
├── kafka/
│   └── producer.py
├── spark/
│   └── spark_streaming.py
├── cassandra/
│   └── init.cql
├── .env
└── README.md
```

