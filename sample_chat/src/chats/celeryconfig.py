from src.config import settings

broker_url = f"redis://{settings.redis_host}:{settings.redis_port}/{settings.redis_broker_db}"
result_backend = f"redis://{settings.redis_host}:{settings.redis_port}/{settings.redis_broker_db}"

task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json']
enable_utc = True
