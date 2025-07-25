# Apache Airflow Base Imports
from airflow import DAG
from airflow.decorators import task
from airflow.sensors.external_task import ExternalTaskMarker
from airflow.sensors.external_task import ExternalTaskSensor
import datetime
# Apache Airflow Custom & DAG/Task Specific Imports
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'airflow',
}

with DAG(
    dag_id="fx_fld_001_app_001",
    start_date=datetime.datetime(2024, 1, 1),
    schedule_interval="@daily",  # TIMEFROM not found, default schedule set to @daily,
    catchup=False,
) as dag:

    # DAG Tasks
    fx_fld_001_app_001_subapp_001_job_001 = BashOperator(
        task_id="fx_fld_001_app_001_subapp_001_job_001",
        bash_command="",
        trigger_rule="all_success",
        dag=dag,
    )

    fx_fld_001_app_001_subapp_001_job_002 = BashOperator(
        task_id="fx_fld_001_app_001_subapp_001_job_002",
        bash_command="",
        trigger_rule="all_success",
        dag=dag,
    )

    fx_fld_001_app_001_subapp_001_job_003 = BashOperator(
        task_id="fx_fld_001_app_001_subapp_001_job_003",
        bash_command="",
        trigger_rule="all_success",
        dag=dag,
    )

    # Airflow Task Internal Dependencies
    fx_fld_001_app_001_subapp_001_job_001 >> [
        fx_fld_001_app_001_subapp_001_job_002, fx_fld_001_app_001_subapp_001_job_003]
    fx_fld_001_app_001_subapp_001_job_002 >> [
        fx_fld_001_app_001_subapp_001_job_003]

    # Airflow Downstream Task Dependencies (external dags)

    fx_fld_001_app_002_subapp_001_job_003_marker_6625 = ExternalTaskMarker(
        task_id="fx_fld_001_app_002_subapp_001_job_003_marker_6625",
        external_dag_id='fx_fld_001_app_002',
        external_task_id='fx_fld_001_app_002_subapp_001_job_003'
    )

    fx_fld_001_app_002_subapp_002_job_005_marker_d7e5 = ExternalTaskMarker(
        task_id="fx_fld_001_app_002_subapp_002_job_005_marker_d7e5",
        external_dag_id='fx_fld_001_app_002',
        external_task_id='fx_fld_001_app_002_subapp_002_job_005'
    )
