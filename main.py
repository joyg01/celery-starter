from datetime import timezone
from celery import Celery
from celery.schedules import crontab
from core.config import settings

# configure broker url
app = Celery(
    'HLT',
    broker=settings.BROKER,
    backend=settings.BACKEND,
    include=[
        "tasks.sample"
        ],
    timezone='UTC'
)

app.conf.beat_schedule = {
    "trigger-scheduled-task": {
        "task": "tasks.sample.scheduled_task",
        # "schedule": crontab() # trigger every minute
        "schedule": crontab(0, 0, day_of_month=1) # trigger every first days of the month
    }
}

if __name__ == '__main__':
    app.start()