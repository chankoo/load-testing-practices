#!/bin/bash

taskId=$(aws ecs list-tasks --cluster cluster-short-link --output text | awk '/cluster-short-link/ {print}' | grep -oE '[a-f0-9]{32}$' | tail -n 1)

aws ecs execute-command --cluster cluster-short-link --task ${taskId} --container short-link --interactive --command "/bin/bash"
