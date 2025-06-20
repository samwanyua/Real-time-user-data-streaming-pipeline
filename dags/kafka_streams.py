from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator

default_args = {
    'owner': 'wanyua',
    'start_date': datetime(2025, 6, 20, 18,00)
}