#!/bin/bash

taskDefinition=$(aws ecs describe-task-definition --task-definition sample-feed --query 'taskDefinition.taskDefinitionArn' --output text)

aws ecs update-service --cluster test-ecs-cluster --service ecs-fargate-sample-feed --task-definition ${taskDefinition} --desired-count 4 --enable-execute-command --force-new-deployment
