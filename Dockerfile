# app/Dockerfile

FROM python:3.9-slim

WORKDIR /app

#RUN apt-get update && apt-get install -y git

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git

RUN git clone https://github.com/madhuranirale1/toolingDS.git .

# Update the Git repository to fetch the latest changes
RUN git pull

RUN pip3 install -r requirements.txt

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "web_app.py", "--server.port=8501", "--server.address=0.0.0.0"]
