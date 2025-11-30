from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator

# Define paths inside the Airflow container
DBT_PROJECT_DIR = "/opt/airflow/include/dbt"
DBT_PROFILES_DIR = "/opt/airflow/include/dbt"

with DAG(
    "dbt_student_performance",
    start_date=datetime(2025, 11, 30),
    schedule="@daily",
    catchup=False,
) as dag:

    dbt_seed = BashOperator(
        task_id="dbt_seed",
        bash_command=f"cd {DBT_PROJECT_DIR} && dbt seed",
        env={
            "DBT_PROFILES_DIR": DBT_PROFILES_DIR,
        },
    )

    dbt_run = BashOperator(
        task_id="dbt_run",
        bash_command=f"cd {DBT_PROJECT_DIR} && dbt run",
        env={
            "DBT_PROFILES_DIR": DBT_PROFILES_DIR,
        },
    )

    dbt_seed >> dbt_run