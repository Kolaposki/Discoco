"""
    name='updater',
    project='discoco'
    date='2/10/2020',
    author='Oshodi Kolapo',
"""
import datetime
import time
from apscheduler.schedulers.background import BackgroundScheduler

from . import sample


def start():
    scheduler = BackgroundScheduler()
    # day_of_week='mon-fri', hour='9', minute='30', second='10',id='task_time'
    scheduler.add_job(sample.massive_scrape_job, 'interval', minutes=3)
    print(f"        ------ Scheduling to scrape for another 24hrs ----\nTime at scheduling : {datetime.datetime.now()}")
    time.sleep(2)
    scheduler.start()


"""

scheduler.add_jobstore(DjangoJobStore(), "default")

DjangoJobExecution.objects.delete_old_job_executions(1800000)  # Delete job executions older than n days calc in millis
@register_job(scheduler, "interval", seconds=60 * 5, id='new03')
def start():
    sample.massive_scrape_job()
    # time.sleep(random.randrange(1, 100, 1) / 100.)
    print(f"Massive Scrape job added at {datetime.datetime.now()}!")


register_events(scheduler)
scheduler.start()
print("Scheduler started!")
"""
