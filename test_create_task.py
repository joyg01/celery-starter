from celery import Celery

# configure broker url
app = Celery(
    'HLT', 
    broker = 'redis://localhost:6379/0',
    backend = 'redis://localhost:6379/0',
    include=["tasks.sample"]
)

app.send_task('tasks.sample.hello')
