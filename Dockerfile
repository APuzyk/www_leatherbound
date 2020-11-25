FROM python:3.7-slim-stretch

# RUN apt-get update && apt-get install nginx vim -y --no-install-recommends

RUN mkdir -p /opt/app
RUN mkdir -p /opt/app/pip_cache
RUN mkdir -p /opt/app/leatherbound
RUN mkdir -p /opt/models
COPY predictor.p /opt/models
COPY requirements.txt start-server.sh /opt/app/
COPY mr_modeling-0.0.1-py3-none-any.whl /opt/app
COPY leatherbound_www /opt/app/leatherbound_www/

WORKDIR /opt/app
RUN pip install torch==1.7.0+cpu -f https://download.pytorch.org/whl/torch_stable.html
RUN pip install /opt/app/mr_modeling-0.0.1-py3-none-any.whl --no-cache-dir
RUN rm /opt/app/mr_modeling-0.0.1-py3-none-any.whl
RUN pip install -r requirements.txt --no-cache-dir
RUN chown -R www-data:www-data /opt/app

RUN export DJANGO_PROD="True"
RUN export DJANGO_SECRET_KEY="J6H90+SHXlp3YGxtt5PQoLDcDO5XlwePz6BnoHu7b4jiSVSMvm"

EXPOSE 8010
STOPSIGNAL SIGTERM
CMD ["/opt/app/start-server.sh"]