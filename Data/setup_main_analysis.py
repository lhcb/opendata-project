# Setup the notebook and download the data
from __future__ import print_function
from __future__ import division

import hashlib
import os
import functools
import warnings
import urllib
warnings.filterwarnings("ignore")

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

def download_data(filename, url, expected_hash):
    while not os.path.isfile(filename):
        try:
            print('Downloading', filename)
            urllib.urlretrieve (url, filename)
        except Exception:
            if not os.path.isfile(filename):
                continue
        _hash = hashlib.md5(open(filename, 'rb').read()).hexdigest()
        if _hash != expected_hash:
            print('Hash does not match for', filename, '- retrying')
            os.remove(filename)

download_data(
    'B2HHH_MagnetDown.root',
    'https://cernbox.cern.ch/index.php/s/gPi4yJkPZrSBenW/download',
    '7901d0070a0c74a13755f6878f420e92'
)
download_data(
    'B2HHH_MagnetUp.root',
    'https://cernbox.cern.ch/index.php/s/8rckTojLRJuEfTF/download',
    'a2ccdd0441b9942f92929390c3b5221e'
)
