FROM mysql:latest

# 환경 변수 설정
ENV MYSQL_DATABASE=sample_feed \
    MYSQL_ROOT_PASSWORD=root

COPY ./mysql-init-files /docker-entrypoint-initdb.d
COPY ./mysql-confs /etc/mysql/conf.d/

EXPOSE 3306