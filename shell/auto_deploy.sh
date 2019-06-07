#!/bin/bash

#if changed Dockerfile, rebuild Docker image
before=`cat ./python/* | md5sum` \
&& git pull && after=`cat ./python/* | md5sum` \
&& if [[ "$before" != "$after" ]]; then docker-compose down && docker-compose up -d --build;fi \
&& docker-compose run python ./manage.py migrate