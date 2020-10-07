from datetime import datetime                                   
from apscheduler.schedulers.blocking import BlockingScheduler

from MainMsg import MainMsg                                #Importing MainMsg Function From Mainmsg.py

sched = BlockingScheduler()
sched.add_job(MainMsg, 'interval', seconds=10)              #Sched.add_job(Function used in MainMsg.py, timeinterval argument, Time in hours, seconds, minutes)

sched.start()                                               #initialising Scheduler
