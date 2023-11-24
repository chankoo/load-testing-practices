#!/bin/bash

taskDefinition=$(aws ecs describe-task-definition --task-definition celery-feed --query 'taskDefinition.taskDefinitionArn' --output text)

aws ecs update-service --cluster test-ecs-cluster --service ecs-fargate-celery-feed-0 --task-definition ${taskDefinition} --desired-count 2 --enable-execute-command --force-new-deployment
