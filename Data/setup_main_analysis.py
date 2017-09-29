# Setup the notebook and download the data
from __future__ import print_function
from __future__ import division

import functools
import hashlib
import os
import warnings
from subprocess import check_output

import numpy
from ipywidgets import interact
import pandas
from root_pandas import read_root
from scipy import stats as st
from matplotlib import pyplot as plt


warnings.filterwarnings("ignore")
rcParams['image.cmap'] = 'Blues'  # change default colormap
pandas.set_option('display.max_columns', None)


def check_hash(filename, fn_hash, block_size=65536):
    if not os.path.isfile(filename):
        return False

    hasher = hashlib.sha256()
    with open(filename, 'rb') as afile:
        buf = afile.read(block_size)
        while len(buf) > 0:
            hasher.update(buf)
            buf = afile.read(block_size)

    if hasher.hexdigest() == fn_hash:
        return True
    else:
        print(filename, 'did not match expected hash, retrying')
        os.remove(filename)
        return False


try:
    # Ensure this doesn't run twice
    new_hist
except NameError:
    _hist = pandas.Series.hist

    @functools.wraps(_hist)
    def new_hist(self, *args, **kwargs):
        kwargs['histtype'] = 'step'
        kwargs['grid'] = False
        return _hist(self, *args, **kwargs)

    pandas.Series.hist = new_hist


def get_plot_func(data):
    def plot_hist(bins, x_min, x_max):
        data.hist(bins=bins, range=(x_min, x_max))
        plt.xlabel('Mass of B+ (MeV/c^2)')
        plt.ylabel('Number of Events')
    return plot_hist


eos_server = 'root://eospublic.cern.ch/'
data_dir = '/eos/opendata/lhcb/AntimatterMatters2017/data/'
filenames = {
    'B2HHH_MagnetDown.root': 'b98651b24f825979053544c37010cf7ef9ce5c56ee62357c7e4ae2c392068379',
    'B2HHH_MagnetUp.root': 'c42ad9e47931e1404bf94ad82ea22a0acd10bc9cfbb58e77a6b0fff08ead7859',
}

for fn, fn_hash in filenames.items():
    while not check_hash('Data/'+fn, fn_hash):
        fn_url = eos_server + data_dir + fn
        print('Downloading', fn_url)
        check_output('xrdcp ' + fn_url + ' ./Data/', shell=True)
