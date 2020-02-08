"""
    name='tasks.py',
    project='discoco'
    date='2/8/2020',
    author='Oshodi Kolapo',
"""

import datetime
import celery
import schedule


@celery.decorators.periodic_task(
    run_every=datetime.timedelta(minutes=1))  # here we assume we want it to be run every 5 mins
def myTask():
    # Do something here
    # like accessing remote apis,
    # calculating resource intensive computational data
    # and store in cache
    # or anything you please
    print('This wasnt so difficult')
