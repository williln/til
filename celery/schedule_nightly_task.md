# Scheduling a nightly Celery task with Celery Beat

We have a task in `myapp/tasks.py`:

```python
from celery import shared_task
from myapp.utils import do_process

@shared_task
def process_task():
    """ Task to do a process """
    do_process()

```

We have already set up Celery and Celery Beat in Docker with compose. 

We want to run the `process_task` task every night. 

Add the celery beat schedule setting to `settings.py`:

```python
from celery.schedules import crontab
CELERY_BEAT_SCHEDULE = {
    "process_task": {
        "task": "myapp.tasks.process_task",
        "schedule": crontab(minute=0, hour=0)
    }

}
```

## Cheat sheet for `schedule` attribute 

| Example                                               | Meaning                                                                                           |
|-------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| `crontab()`                                           | Execute every minute.                                                                             |
| `crontab(minute=0, hour=0)`                           | Execute daily at midnight.                                                                        |
| `crontab(minute=0, hour='*/3')`                       | Execute every three hours: midnight, 3am, 6am, 9am, noon, 3pm, 6pm, 9pm.                          |
| `crontab(minute=0, hour='0,3,6,9,12,15,18,21')`       | Same as previous.                                                                                 |
| `crontab(minute='*/15')`                              | Execute every 15 minutes.                                                                         |
| `crontab(day_of_week='sunday')`                       | Execute every minute (!) at Sundays.                                                              |
| `crontab(minute='*', hour='*', day_of_week='sun')`    | Same as previous.                                                                                 |
| `crontab(minute='*/10', hour='3,17,22', day_of_week='thu,fri')` | Execute every ten minutes, but only between 3-4 am, 5-6 pm, and 10-11 pm on Thursdays or Fridays. |
| `crontab(minute=0, hour='*/2,*/3')`                   | Execute every even hour, and every hour divisible by three.                                       |
| `crontab(minute=0, hour='*/5')`                       | Execute hour divisible by 5. This means that it is triggered at 3pm, not 5pm.                     |
| `crontab(minute=0, hour='*/3,8-17')`                  | Execute every hour divisible by 3, and every hour during office hours (8am-5pm).                  |
| `crontab(0, 0, day_of_month='2')`                     | Execute on the second day of every month.                                                         |
| `crontab(0, 0, day_of_month='2-30/2')`                | Execute on every even numbered day.                                                               |
| `crontab(0, 0, day_of_month='1-7,15-21')`             | Execute on the first and third weeks of the month.                                                |
| `crontab(0, 0, day_of_month='11', month_of_year='5')` | Execute on the eleventh of May every year.                                                        |
| `crontab(0, 0, month_of_year='*/3')`                  | Execute every day on the first month of every quarter.                                            |
