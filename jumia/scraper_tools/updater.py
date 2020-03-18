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
    scheduler.add_job(sample.massive_scrape_job, 'interval', minutes=55, max_instances=2)
    print(f"       ------ Scheduling to scrape for another 55 mins ----\nTime at scheduling : {datetime.datetime.now()}")
    time.sleep(2)
    scheduler.start()
