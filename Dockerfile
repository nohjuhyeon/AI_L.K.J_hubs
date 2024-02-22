FROM python:3.11

# OpenJDK 설치 (예시로 OpenJDK 17을 설치)
RUN apt-get update && \
    apt-get install -y openjdk-17-jdk fonts-nanum && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# JAVA_HOME 환경 변수 설정
ENV JAVA_HOME /usr/lib/jvm/java-17-openjdk-amd64

# 작업 디렉토리 설정
WORKDIR /app

ARG BRANCH_NAME=data_engineers
ARG DIR_NAME=AI_L.K.J_hubs # 변경대상

# Clone the Git repository. Here we dynamically specify the repository name using the variable defined earlier.
# RUN git clone -b ${BRANCH_NAME} https://github.com/gocolab/co_templates ${DIR_NAME}
RUN git clone https://github.com/nohjuhyeon/AI_L.K.J_hubs ${DIR_NAME}
# Changes the working directory to /app/${REPO_NAME}. This uses the variable to dynamically set the directory path.
WORKDIR /app/${DIR_NAME}

# RUN pip install --no-cache-dir -r ./requirements.txt
RUN pip install -r ./requirements.txt

# RUN rm -rf .git

