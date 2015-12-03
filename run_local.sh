#!/bin/bash

set -e
WORKDIR=`pwd`

C_ANADIR="/home/jupyter/analysis"

# Unclear why exactly you need to run the notebook with `sh -c`
# Found this solution from ipython/ipython#7062 and ipython/docker-notebook#6
container_id=`docker run -d -v $WORKDIR:$C_ANADIR -p 8888 betatim/everware-demo sh -c "ipython notebook --port=8888 --ip=0.0.0.0 --no-browser --notebook-dir=$C_ANADIR"`

if hash docker-machine 2>/dev/null; then
    connect_string=`docker port $container_id 8888 | sed -e 's/0.0.0.0/'$(docker-machine ip docker-vm)'/'`
elif hash boot2docker 2>/dev/null; then
    connect_string=`docker port $container_id 8888 | sed -e 's/0.0.0.0/'$(boot2docker ip)'/'`
else
    connect_string=`docker port $container_id 8888`
fi

echo "Once you are done run the following two commands to clean up:"
echo
echo "    docker stop "$container_id
echo "    docker rm "$container_id
echo
echo "To get started point your browser at: "$connect_string
