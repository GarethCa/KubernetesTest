#!/bin/sh
docker image rm docker_test --force

docker build -t docker_test .