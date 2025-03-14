#!/bin/sh
VERSION=0.1.0
APP_NAME="siewdai-android"

docker build -t $APP_NAME:$VERSION .
docker run -it --rm $APP_NAME
