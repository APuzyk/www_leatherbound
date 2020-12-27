FROM python:3.7-slim-stretch

RUN mkdir -p /opt/app
RUN mkdir -p /opt/app/pip_cache
RUN mkdir -p /opt/app/leatherbound
RUN mkdir -p /opt/models

COPY sentiment_helper.p /opt/models
COPY sentiment.onnx /opt/models
COPY requirements.txt start-server.sh /opt/app/
COPY leatherbound_www /opt/app/leatherbound_www/

WORKDIR /opt/app
#RUN pip install torch==1.7.0+cpu -f https://download.pytorch.org/whl/torch_stable.html
#RUN pip install /opt/app/mr_modeling-0.0.1-py3-none-any.whl --no-cache-dir
#RUN rm /opt/app/mr_modeling-0.0.1-py3-none-any.whl
# RUN apt-get update && \
#     apt-get upgrade -y && \
#     apt-get install  libpq-dev && \
#     apt-get install --virtual .build-deps gcc musl-dev && \
#     apt-get clean

# RUN pip install -r requirements.txt --no-cache-dir
RUN set -ex \
    && BUILD_DEPS=" \
    build-essential \
    libpcre3-dev \
    libpq-dev \
    " \
    && apt-get update && apt-get install -y --no-install-recommends $BUILD_DEPS \
    && pip install --no-cache-dir -r requirements.txt \
    \
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false $BUILD_DEPS \
    && rm -rf /var/lib/apt/lists/*
RUN chown -R www-data:www-data /opt/app

EXPOSE 8010
STOPSIGNAL SIGTERM
CMD ["/opt/app/start-server.sh"]