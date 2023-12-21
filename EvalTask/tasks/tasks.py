from celery import shared_task
from datetime import datetime
from time import sleep

@shared_task
def print_task_name(task_name):
    # Simulate a task that takes some time to execute
    sleep(5)
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Task '{task_name}' executed at {now}")