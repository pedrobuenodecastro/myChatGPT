#!/bin/bash

# build the docker image
docker build -t my-chatgpt .

# Run the container in detached mode and mount the log volume
docker run -d -v $PWD/log:/app/log -v $PWD/app/key:/app/key my-chatgpt

# Get the ID of the running container
container_id=$(docker ps -q)

# Execute the command to start a bash session
docker exec -it $container_id /bin/bash
