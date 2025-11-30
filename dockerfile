FROM apache/airflow:3.1.3-python3.11

USER root

RUN apt-get update && apt-get install -y build-essential
USER airflow

# Install dbt + duckdb
#COPY requirements.txt /opt/airflow/requirements.txt
#RUN pip install -r /opt/airflow/requirements.txt
RUN pip install dbt-duckdb