FROM mysql:latest

# 환경 변수 설정(short_link 테이블 생성)
ENV MYSQL_DATABASE=short_link \
    MYSQL_ROOT_PASSWORD=root

COPY ./mysql-init-files /docker-entrypoint-initdb.d
COPY ./mysql-confs /etc/mysql/conf.d/

EXPOSE 3306