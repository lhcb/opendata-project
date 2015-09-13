FROM betatim/roofit-tutorial:14082015
MAINTAINER Tim Head <betatim@gmail.com>

USER root
RUN conda install -n py27 --yes numpy==1.9.2
RUN /bin/bash -c "source activate py27 && pip install rootpy==0.8.0 root_numpy==4.3.0"

USER jupyter