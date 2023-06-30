# Pull base image
FROM python:3.11-bullseye

# Set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
# ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# work around librdkafka arm64 issue
RUN apt-get update && \
  apt-get install -y --no-install-recommends gcc git libssl-dev g++ make && \
  cd /tmp && git clone https://github.com/edenhill/librdkafka && \
  cd librdkafka && git checkout tags/v2.1.1 && \
  ./configure --install-deps && make && make install && \
  ldconfig &&\
  cd ../ && rm -rf librdkafka

RUN pip install confluent-kafka==2.0.2

# Install dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Copy project
COPY . .
