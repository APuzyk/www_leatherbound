FROM python:3.7-slim-stretch

RUN apt-get update && apt-get install nginx vim -y --no-install-recommends
COPY nginx.default /etc/nginx/sites-available/default
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log

RUN mkdir -p /opt/app
RUN mkdir -p /opt/app/pip_cache
RUN mkdir -p /opt/app/leatherbound
RUN mkdir -p /opt/models
COPY predictor.p /opt/models
COPY requirements.txt start-server.sh /opt/app/
COPY mr_modeling-0.0.1-py3-none-any.whl /opt/app
COPY leatherbound_www /opt/app/leatherbound_www/

RUN mkdir -p /opt/app/leatherbound_fe
COPY elm.js /opt/app/leatherbound_fe
COPY index.html /opt/app/leatherbound_fe

WORKDIR /opt/app
RUN pip install torch==1.7.0+cpu torchvision==0.8.1+cpu torchaudio==0.7.0 -f https://download.pytorch.org/whl/torch_stable.html
RUN pip install /opt/app/mr_modeling-0.0.1-py3-none-any.whl --no-cache-dir
RUN rm /opt/app/mr_modeling-0.0.1-py3-none-any.whl
RUN pip install -r requirements.txt --no-cache-dir
RUN chown -R www-data:www-data /opt/app

EXPOSE 8080
STOPSIGNAL SIGTERM
CMD ["/opt/app/start-server.sh"]