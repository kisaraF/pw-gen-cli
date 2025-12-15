# Base image python slim will reduce size by 60-70% vs full images
FROM python:3.11-slim

# This will make sure stderr and stdout to appear without staying in buffer (memory)
ENV PYTHONUNBUFFERED=1

# Default to /app directory within docker container for everything coming in the ops
WORKDIR /app


# ---------- BUILDING FROM THE WHEEL FILE
# Let's copy the wheel file
# COPY dist/*.whl /app/

# Now install the wheel file
# RUN pip install --no-cache-dir /app/*.whl



# ---------- BUILDING FROM THE SOURCE
# Let's copy all the required files
COPY pw_gen_cli ./pw_gen_cli
COPY requirements.txt ./
COPY pyproject.toml ./

RUN pip install --no-cache-dir uv
RUN uv pip install --system .



# Defaulting to bash to usage
CMD ["bash"]