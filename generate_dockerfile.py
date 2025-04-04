#!/usr/bin/env python3
import toml
import os

def generate_dockerfile(config_file="honeycore_saga.toml",
                        output_file="Dockerfile"):
    data = toml.load(config_file)
    docker_cfg = data.get("docker", {})

    base_image       = docker_cfg.get("base_image", "ubuntu:latest")
    python_version   = docker_cfg.get("python_version", "3.11")
    venv_name        = docker_cfg.get("venv_name", "honeycore_env")
    dev_mount        = docker_cfg.get("dev_mount", "/dev/honeycore")
    
    dockerfile_content = (
        f"FROM {base_image}\n\n"
        "# Install Python3 and virtualenv dependencies\n"
        "RUN apt-get update && \\\n"
        "    apt-get install -y python3 python3-venv python3-pip && \\\n"
        "    apt-get clean && rm -rf /var/lib/apt/lists/*\n\n"
        "# Set working directory\n"
        "WORKDIR /app\n\n"
        "# Create virtual environment\n"
        f"RUN python3 -m venv {venv_name}\n"
        "ENV PATH=\"/app/{}/bin:$PATH\"\n\n".format(venv_name) +
        "# Create development mount point\n"
        f"RUN mkdir -p {dev_mount}\n\n"
        "# Default command\n"
        'CMD [ "python3" ]\n'
    )

    with open(output_file, "w") as f:
        f.write(dockerfile_content)
    print(f"Dockerfile generated at: {output_file}")

if __name__ == "__main__":
    generate_dockerfile()
