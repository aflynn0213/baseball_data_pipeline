from airflow import settings
from airflow.configuration import conf

def configure_airflow():
    settings.configure()

    conf.set("core", "sql_alchemy_conn", "sqlite:////tmp/airflow.db")
