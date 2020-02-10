"""
    name='updater',
    project='discoco'
    date='2/10/2020',
    author='Oshodi Kolapo',
"""
import datetime

from apscheduler.schedulers.background import BackgroundScheduler
from . import sample


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(sample.massive_scrape_job, 'interval', minutes=60*24)
    print(f"        ------ Scheduling to scrape for another 24hrs ----\nTime at scheduling : {datetime.datetime.now()}")
    scheduler.start()
