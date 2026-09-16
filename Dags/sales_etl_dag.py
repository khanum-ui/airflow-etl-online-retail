from datetime import datetime

from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator


with DAG(
    dag_id="sales_etl_pipeline",
    start_date=datetime(2026, 9, 15),
    schedule=None,
    catchup=False,
    tags=["ETL", "Sales"],
) as dag:

    extract = BashOperator(
        task_id="extract",
        bash_command="python /opt/airflow/project/Script/extract.py",
    )

    transform = BashOperator(
        task_id="transform",
        bash_command="python /opt/airflow/project/Script/transform.py",
    )

    load = BashOperator(
        task_id="load",
        bash_command="python /opt/airflow/project/Script/load.py",
    )

    validate = BashOperator(
        task_id="validate",
        bash_command="python /opt/airflow/project/Script/validate.py",
    )

    extract >> transform >> load >> validate