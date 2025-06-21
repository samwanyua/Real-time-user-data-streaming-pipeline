#!/bin/bash
pip install -r /opt/airflow/requirements.txt
airflow db upgrade
exec airflow webserver
