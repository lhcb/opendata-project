FROM chrisburr/opendata:v2
MAINTAINER Christopher Burr <c.b@cern.ch>

USER root
COPY _start_jupyter.sh /srv/singleuser/singleuser.sh
RUN echo "Welcome to the LHCb open data container"
