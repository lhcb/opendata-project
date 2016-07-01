#!/bin/bash

if [ -z "$JPY_WORKDIR" ] ; then
  export JPY_WORKDIR="/notebooks"
fi

if [ ! -d $JPY_WORKDIR ] ; then
  mkdir -p $JPY_WORKDIR
fi

if [ -n "$JPY_GITHUBURL" ] ; then
  git clone $JPY_GITHUBURL $JPY_WORKDIR > $HOME/git.log
  git reset --hard $JPY_REPOPOINTER
  jupyterhub-singleuser \
    --port=8888 \
    --ip=0.0.0.0 \
    --user=$JPY_USER \
    --cookie-name=$JPY_COOKIE_NAME \
    --base-url=$JPY_BASE_URL \
    --hub-prefix=$JPY_HUB_PREFIX \
    --hub-api-url=$JPY_HUB_API_URL \
    --notebook-dir=$JPY_WORKDIR
else
  jupyter notebook --no-browser --ip=0.0.0.0 --notebook-dir=$JPY_WORKDIR
fi
