import sys
from time import sleep
from apscheduler.scheduler import Scheduler
sched = Scheduler()
sched.start()        # start the scheduler

# define the function that is to be executed
# it will be executed in a thread by the scheduler
def my_job(text):
    print text

def main():
    # job = sched.add_date_job(my_job, datetime(2013, 8, 5, 23, 47, 5), ['text'])
    job = sched.add_date_job(my_job, '2013-08-05 23:47:05', ['text'])
    while True:
        sleep(1)
        sys.stdout.write('.'); sys.stdout.flush()

##############################################################

if __name__ == "__main__":
    main()