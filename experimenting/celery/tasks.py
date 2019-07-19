from celery import Celery

# Defining the app like this wont enable results. To enable results we 
# need to configure Celery to use a result backend.
# app = Celery('tasks', broker='redis://localhost:6379')

# Defining the backend as redis
app = Celery('tasks', backend='redis://localhost', 
        broker='redis://localhost')


@app.task
def add(x, y):
    return x + y
