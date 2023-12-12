#!/bin/bash

python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. ./src/core/id_generator.proto

alembic upgrade head

uvicorn src.main:app --host 0.0.0.0 --port 8080 --reload