from __future__ import print_function
from __future__ import division

import warnings
warnings.filterwarnings("ignore")

import pandas 
import math
from ipywidgets import interact

pandas.options.mode.chained_assignment = None
data = pandas.read_csv('Data/nobel.csv', ',')

rcParams['image.cmap'] = 'Blues'  # change default colormap

def parse_year(s):
    try:
        if s[-3] == '-':
            return int('19' + s[-2:])
        elif s[-4:] == 'Data':   # If there is a value of no data set the age to something
            return 1000          # Large that we can filter later
        else:
            return int(s[-4:])
    except Exception:
        return 1000

data['BirthYear'] = data['Birthdate'].apply(parse_year)
data = data.query('BirthYear > 1000')