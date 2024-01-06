#!/bin/bash

taskDefinition=$(aws ecs describe-task-definition --task-definition sample-chat --query 'taskDefinition.taskDefinitionArn' --output text)

aws ecs update-service --cluster cluster-sample-chat --service service-sample-chat-0 --task-definition ${taskDefinition} --desired-count 1 --enable-execute-command --force-new-deployment
