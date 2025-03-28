import pendulum
from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator

with DAG(
    "large_dag",
    schedule=None,
    start_date=(pendulum.datetime(2024, 12, 1, tz="UTC")),
):
    for i in range(50):
        BashOperator(
            task_id=f"task_{i}",
            bash_command="true",
            cwd=".",
        )
