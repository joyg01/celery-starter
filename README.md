

Run docker
```
docker run -d -p 6379:6379 redis
```

Run Celery
```
celery -A main worker --loglevel=INFO
```
Run Beats
```
celery -A main beat --loglevel=INFO
```

Run Flower
```
flower -A main --port=5555
```