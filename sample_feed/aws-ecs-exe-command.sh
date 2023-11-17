#!/bin/bash

taskId=$(aws ecs list-tasks --cluster test-ecs-cluster --output text | awk '/test-ecs-cluster/ {print}' | grep -oE '[a-f0-9]{32}$' | tail -n 1)

aws ecs execute-command --cluster test-ecs-cluster --task ${taskId} --container sample-feed --interactive --command "/bin/bash"
