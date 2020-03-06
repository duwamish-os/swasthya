FROM centos

RUN yum update -y
RUN yum install -y python3

RUN mkdir -p /usr/local/app/
COPY health_check.py /usr/local/app/ 


ENTRYPOINT ["python3 /usr/local/app/health_check.py"]
