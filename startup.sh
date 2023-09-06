#!/bin/sh
set -e

gunicorn -k geventwebsocket.gunicorn.workers.GeventWebSocketWorker -w 1 --threads $APP_THREADS -b 0.0.0.0:$APP_PORT wsgi:app