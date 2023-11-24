#!/bin/bash

aws ecs register-task-definition --cli-input-json file://./aws-ecs-task-definition-celery-feed.json