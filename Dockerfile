FROM centos

ENV PYTHONUNBUFFERED=0

RUN yum update -y
RUN yum install -y python3

RUN mkdir -p /usr/local/app/
COPY health_check.py /usr/local/app/health_check.py
COPY application.ini /usr/local/app/application.ini

RUN python3 --version

ENTRYPOINT ["python3", "/usr/local/app/health_check.py"]
