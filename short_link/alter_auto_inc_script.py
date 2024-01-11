from sqlalchemy import create_engine, text
from src.config import settings
from src.database import DATABASE_URL_SYNC

# 데이터베이스 연결 문자열 설정
engine = create_engine(DATABASE_URL_SYNC)

# SQL 쿼리 작성
sql_query = text("ALTER TABLE short_url AUTO_INCREMENT = 3844")

# 쿼리 실행
with engine.connect() as connection:
    connection.execute(sql_query)
