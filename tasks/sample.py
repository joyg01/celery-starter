from main import app


@app.task
def hello():
    return {"Hello":"World"}


@app.task
def scheduled_task():
    return {"Hi":"Iam A Scheduled Task"}

