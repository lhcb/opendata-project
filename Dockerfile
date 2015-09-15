FROM betatim/roofit-tutorial:14082015
MAINTAINER Tim Head <betatim@gmail.com>

USER root
RUN conda install -n py27 --yes numpy==1.9.2
RUN conda install -n py27 --yes matplotlib==1.4.3
RUN conda install -n py27 --yes scipy==0.16.0
RUN /bin/bash -c "source activate py27 && pip install rootpy==0.8.0 root_numpy==4.3.0"

# modified version of the cling kernel
# this uses cling as packaged with ROOT
USER jupyter
RUN echo 1> /dev/null && git clone https://github.com/betatim/clingkernel.git
USER root
RUN conda install --yes pexpect
RUN cd clingkernel && pip install -e . && ipython kernelspec install cling

USER jupyter