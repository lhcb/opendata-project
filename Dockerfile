FROM betatim/everware_cern_analysis:31102015
MAINTAINER Tim Head <betatim@gmail.com>

USER root
RUN apt-get -y update && apt-get install -y curl

USER jupyter
RUN /bin/bash -c "source activate py27 && conda install pandas numexpr && pip install rootpy==0.8.0 root_numpy==4.3.0"
RUN /bin/bash -c "source activate py27 && conda install -n py27 ipywidgets==4.1.0"
RUN /bin/bash -c "source activate py27 && pip install https://github.com/ipython-contrib/IPython-notebook-extensions/archive/master.zip"
RUN /bin/bash -c "source activate py27 && jupyter nbextension enable usability/collapsible_headings/main"
