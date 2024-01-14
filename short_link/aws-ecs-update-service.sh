#!/bin/bash

taskDefinition=$(aws ecs describe-task-definition --task-definition short-link --query 'taskDefinition.taskDefinitionArn' --output text)

aws ecs update-service --cluster cluster-short-link --service service-short-link --task-definition ${taskDefinition} --desired-count 2 --enable-execute-command --force-new-deployment
