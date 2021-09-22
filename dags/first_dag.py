import airflow
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'sibitenda harriet',
    'start_date': days_ago(1)
    }

# Defining the DAG using Context Manager
with DAG(
        'extract-meeting-activities',
        default_args=default_args,
        schedule_interval=None,
        ) as dag:
        t1 = BashOperator(
                task_id = 'extract_metadata_from_text',
                bash_command = 'C:\Users\DELL\airflow-tutorial\first-workflow\extract_metadata.py',
        )

       # t1 >>  # Defining the task dependencies
