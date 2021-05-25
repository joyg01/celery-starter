import os

class Settings():
    BROKER:str = os.environ.get("CELERY_BROKER", "redis://localhost:6379/0")
    BACKEND:str = os.environ.get("CELERY_BACKEND", "redis://localhost:6379/0")


settings = Settings()