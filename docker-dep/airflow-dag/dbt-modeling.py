from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import timedelta, datetime


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'run-dbt-models',
    default_args=default_args,
    description='A DAG to run dbt models',
    schedule_interval=timedelta(days=1)
)

#task
dbtmodel = BashOperator(
    task_id = 'dbt-model',

    bash_command=' && '.join([
            'cd /opt/airflow/dags/dbt-profiles',
            # 'source .venv/Scripts/activate',
            'export DBT_PROFILES_DIR=$(pwd)', 
            'cd ../dbt-project',
            'dbt run',
    ]),
    dag=dag  
)


dbtmodel 

