#!/bin/bash

aws ecs register-task-definition --cli-input-json file://./aws-ecs-task-definition-sample-chat.json