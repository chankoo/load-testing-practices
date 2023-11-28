# Use the official PostgreSQL image as the base image
FROM postgres

# Set environment variables for the database
ENV POSTGRES_DB=sample_chat POSTGRES_USER=root POSTGRES_PASSWORD=root

COPY ./postgres-init-files /docker-entrypoint-initdb.d
COPY ./postgres-conf/ /etc/postgresql/

# The default port for PostgreSQL is 5432, expose it
EXPOSE 5432
