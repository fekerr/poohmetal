FROM ubuntu:latest

# Install Python3 and virtualenv dependencies
RUN apt-get update && \
    apt-get install -y python3 python3-venv python3-pip && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Create virtual environment
RUN python3 -m venv honeycore_env
ENV PATH="/app/honeycore_env/bin:$PATH"

# Create development mount point
RUN mkdir -p /dev/honeycore

# Default command
CMD [ "python3" ]
