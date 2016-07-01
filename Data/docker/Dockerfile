FROM everware/base:23102015
MAINTAINER Chris Burr <c.b@cern.ch>

USER root
RUN apt-get -y update
# Things needed to build ROOT
RUN apt-get -y --force-yes install libx11-dev libxpm-dev libxft-dev libxext-dev libpng3 libjpeg8 gfortran libssl-dev libpcre3-dev libgl1-mesa-dev libglew1.5-devibftgl-dev libmysqlclient-dev libfftw3-dev libcfitsio3-dev graphviz-dev libavahi-compat-libdnssd-dev libldap2-dev libxml2-dev libafterimage0 libafterimage-dev cmake vimmacs zsh krb5-user krb5-config curl

WORKDIR /tmp

# ROOT from source, because that is how we roll
#
# built with python2.7 take care to install all python modules for this
# version of python later on
RUN /bin/bash -c "source activate py27 \
    && git clone --depth 1 http://root.cern.ch/git/root.git -b v6-04-16 --single-branch \
    && mkdir root-build \
    && cd root-build \
    && cmake ../root -Droofit=ON -Dhdfs=OFF -Dbuiltin_xrootd=ON -DCMAKE_INSTALL_PREFIX=/usr/local \
    && make -j3 \
    && cmake --build . --target install \
    && cd .. \
    && rm -rf root root-build"
RUN /bin/bash -c "source activate py27 \
    && git clone --depth 1 http://github.com/xrootd/xrootd.git -b v4.2.3 --single-branch \
    && mkdir xrootd-build \
    && cd xrootd-build \
    && cmake ../xrootd -DCMAKE_INSTALL_PREFIX=/usr/local -DENABLE_PERL=FALSE -DENABLE_FUSE=FALSE \
    && make && make install \
    && cd .. && rm -rf xrootd xrootd-build"

ENV LD_LIBRARY_PATH /usr/local/lib:$LD_LIBRARY_PATH
ENV PYTHONPATH /usr/local/lib:$PYTHONPATH

ADD krb5.conf /etc/krb5.conf
ADD save-to-cernbox.sh /usr/local/bin/save-to-cernbox.sh
ADD cb-get.sh /usr/local/bin/cb-get.sh
ADD cb-put.sh /usr/local/bin/cb-put.sh

USER jupyter
WORKDIR /home/jupyter

RUN conda install -n py27 --yes numpy==1.9.2 scipy==0.16.0 matplotlib==1.4.3

RUN /bin/bash -c "source activate py27 \
       && python -c \"import os;import json;f='/home/jupyter/.local/share/jupyter/kernels/python2/kernel.json';j=json.load(open(f));j['env']={'PATH':s.environ['PATH']};json.dump(j,open(f,'w'))\""

ADD bashrc /home/jupyter/.bashrc
ADD root-kernel.json /home/jupyter/.local/share/jupyter/kernels/root/kernel.json
ADD root-logo-32x32.png /home/jupyter/.local/share/jupyter/kernels/root/logo-32x32.png
ADD root-logo-64x64.png /home/jupyter/.local/share/jupyter/kernels/root/logo-64x64.png

RUN /bin/bash -c "source activate py27 && conda install -y pandas numexpr && pip install rootpy==0.8.0 root_numpy==4.3.0"
RUN /bin/bash -c "source activate py27 && pip install ipywidgets==5.0.0"
RUN /bin/bash -c "source activate py27 && pip install https://github.com/ipython-contrib/IPython-notebook-extensions/archive/master.zip"
RUN /bin/bash -c "source activate py27 && jupyter nbextension enable usability/collapsible_headings/main"
RUN /bin/bash -c "source activate py27 && jupyter nbextension enable --py widgetsnbextension"

RUN /bin/bash -c "source activate py27 && pip install root_pandas"

RUN /bin/bash -c "source activate root && pip install ipywidgets==5.0.0"
RUN /bin/bash -c "source activate root && jupyter nbextension enable --py widgetsnbextension"
