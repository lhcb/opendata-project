# Setup the notebook and download the data
from __future__ import print_function
from __future__ import division

import functools
import warnings
warnings.filterwarnings("ignore")
from subprocess import check_output

import numpy
from ipywidgets import interact
import pandas

rcParams['image.cmap'] = 'Blues'  # change default colormap

pandas.set_option('display.max_columns', None)

# TODO Prevent this happening twice
_hist = pandas.Series.hist
@functools.wraps(_hist)
def new_hist(self, *args, **kwargs):
    kwargs['histtype'] = 'step'
    kwargs['grid'] = False
    return _hist(self, *args, **kwargs)
pandas.Series.hist = new_hist

from root_pandas import read_root

from scipy import stats as st
from matplotlib import pyplot as plt


def get_plot_func(data):
    def plot_hist(bins, x_min, x_max):
        data.hist(bins=bins, range=(x_min, x_max))
        plt.xlabel('Mass of B+ (MeV/c^2)')
        plt.ylabel('Number of Events')
    return plot_hist


check_output('xrdcp xroot://eospublic.cern.ch//eos/opendata/lhcb/AntimatterMatters2017/data/B2HHH_MagnetDown.root .')
check_output('xrdcp xroot://eospublic.cern.ch//eos/opendata/lhcb/AntimatterMatters2017/data/B2HHH_MagnetUp.root .')
