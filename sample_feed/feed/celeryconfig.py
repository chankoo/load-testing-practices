from django.conf import settings

broker_url = f"redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}/{settings.REDIS_DB}"
result_backend = f"redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}/{settings.REDIS_DB}"
timezone = "Asia/Seoul"

task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json']
enable_utc = True
