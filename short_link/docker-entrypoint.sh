#!/bin/bash
alembic upgrade head

python alter_auto_inc_script.py

uvicorn src.main:app --host 0.0.0.0 --port 80 --reload