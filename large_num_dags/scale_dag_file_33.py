import pendulum
from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator

for i in range(20):
    with DAG(
            f"scale_dag_file_foo_num_{i}_33",
            schedule=None,
            start_date=(pendulum.datetime(2024, 12, 1, tz="UTC")),
    ):
        for i in range(10):
            BashOperator(
                task_id=f"task_{i}",
                bash_command="true",
                cwd=".",
            )
