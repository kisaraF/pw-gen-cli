# Base image python slim will reduce size by 60-70% vs full images
FROM python:3.11-slim

# This will make sure stderr and stdout to appear without staying in buffer (memory)
ENV PYTHONUNBUFFERED=1

# Default to /app directory within docker container for everything coming in the ops
WORKDIR /app


# ---------- BUILDING FROM THE SOURCE
# Let's copy all the required files
COPY requirements.txt ./
COPY pyproject.toml ./
COPY README.md ./

RUN pip install --no-cache-dir uv

# --system tells to install directly to docker system
RUN uv pip install --system --no-cache -r requirements.txt

COPY src/pw_gen_cli ./src/pw_gen_cli

# The missing piece — installs pw-gen-cli itself,
# which is what actually generates the `pwdgen` executable
RUN uv pip install --system --no-cache .

# Defaulting to bash to usage
# CMD ["bash"]

CMD ["pwdgen", "gen-password"]
