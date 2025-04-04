#!/bin/bash
# Run the Docker container with a folder mount for development
docker run -d --name honeycore_container \
    -v "$(pwd)/dev:/dev/honeycore" \
    honeycore_saga
