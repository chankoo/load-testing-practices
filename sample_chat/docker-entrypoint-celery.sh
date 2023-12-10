#!/bin/bash

celery -A src.chats.celery worker --loglevel=debug