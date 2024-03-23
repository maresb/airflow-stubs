import http.server
from airflow.configuration import conf as conf
from airflow.jobs.job import Job as Job
from airflow.jobs.scheduler_job_runner import SchedulerJobRunner as SchedulerJobRunner
from airflow.utils.net import get_hostname as get_hostname
from airflow.utils.session import create_session as create_session

class HealthServer(http.server.BaseHTTPRequestHandler):
    def do_GET(self): ...
def serve_health_check(): ...
