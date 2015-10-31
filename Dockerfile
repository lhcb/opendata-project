FROM betatim/everware_cern_analysis:31102015
MAINTAINER Tim Head <betatim@gmail.com>

USER root
RUN apt-get install -y curl

USER jupyter
RUN /bin/bash -c "source activate py27 && pip install rootpy==0.8.0 root_numpy==4.3.0"
