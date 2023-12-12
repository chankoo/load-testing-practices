#!/bin/bash

python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. ./id_generator.proto

python server.py