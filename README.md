## Real-Time User Data Streaming Pipeline

A fully containerized, real-time data pipeline for ingesting, processing, and storing user data from the [Random User API](https://randomuser.me). Built using Apache Kafka, Apache Spark Streaming, Apache Cassandra, and orchestrated via Apache Airflow—all running inside Docker.

---

### Overview

This project demonstrates a complete real-time data engineering workflow:

1. **Data Ingestion** – Python scripts fetch synthetic user data from Random User API and push it to Kafka topics.
2. **Streaming Processing** – Apache Spark consumes and processes these events from Kafka in real-time.
3. **Storage** – Cleaned and transformed data is written into Apache Cassandra for durable storage and querying.
4. **Orchestration** – Apache Airflow schedules and manages the end-to-end workflow.

---

### Tech Stack

| Layer        | Technology                |
|--------------|---------------------------|
| Ingestion     | Python, Random User API   |
| Messaging     | Apache Kafka, Apache Zookeeper |
| Processing    | Apache Spark Streaming     |
| Storage       | Apache Cassandra           |
| Orchestration | Apache Airflow             |
| Containerization | Docker, Docker Compose |
| CI/CD         | Github Actions            |

---

### Data Flow Architecture

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

### Running the project with Docker
Requirements: Docker, Docker Compose
```
# Clone the repository
git clone https://github.com/wanyua/Real-time-user-streaming-pipeline.git
cd Real-time-user-streaming-pipeline

# Start the containers
docker-compose up --build

```

Airflow UI: http://localhost:8080
Kafka Broker: localhost:9092
Cassandra DB: localhost:9042

### Testing the Pipeline
Run the Kafka producer to start sending user data:

``` 
docker exec -it kafka-producer python3 producer.py
```
* Monitor Spark logs to confirm data is being processed.

* Connect to Cassandra and query the users table:
``` 
SELECT * FROM user_profiles LIMIT 10;
```

### Features
* Real-time data streaming & processing
* Fault-tolerant Kafka queues
* Schema-on-write with Cassandra
* Modular & reproducible with Docker
* Fully orchestrated with Airflow DAGs

### Future Improvements
* Add monitoring with Prometheus + Grafana
* Use Avro schemas for Kafka data
* Deploy to a cloud platform (GCP/AWS)
* Add data quality checks in Airflow

### Learnings
This project helps reinforce critical concepts in real-time data pipelines, including:
 * Kafka topic design and reliability
 * Spark micro-batch processing
 * Managing distributed services with Docker
 * Workflow orchestration using Airflow

