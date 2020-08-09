#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Mon Jul  6 14:08:44 2020

@author: shino
"""

import numpy as np
import pandas as pd


def read_bin(filename, shape=None, **kwargs):
    """ Read a _raw binary_ file and store all possible elements in pandas DataFrame.
    If the shape of the array is known, it can be specified using `shape`. The
    first three columns are used for x, y and z.  Otherwise the binary file is
    assumed have row-major format, three columns are formed and used as x, y and
    z , respectively.
    NOTE: binary files that are not `raw` will not behave as expected. If they
    contain a header/footer with meta data, or were generated e.g. via Protobuf,
    then bahviour is also undefined.
    Parameters
    ----------
    filename: str
        Path to the filename
    shape: (n_rows, n_cols) - shape to be formed from the loaded binary array, optional.
    **kwargs:
    kwargs: numpy.fromfile supported kwargs
        Check NumPy documentation for all possibilities.
    Returns
    -------
    data: dict
        If possible, elements as pandas DataFrames else a NumPy ndarray
    """
    data = {}
    print(filename)
    kwargs['dtype'] = kwargs.get('dtype', np.float32)
    arr = np.fromfile(filename, **kwargs)
    print(arr[0])
    if shape is not None:
        try:
            arr = arr.reshape(shape)
        except ValueError:
            raise ValueError(('The array cannot be reshaped to {0} as '
                              'it has {1} elements, which is not '
                              'divisible by three'.format(shape, arr.size)))
    else:
        arr = arr.reshape((-1, 3))

    data["points"] = pd.DataFrame(arr[:, 0:3], columns=['x', 'y', 'z'])

    return data

def main():

#    path = "/Volumes/ssd/diamond.bin"
#    print(path)
    path = "/Volumes/ssd/NYU/all/T_316000_233500_NW.bin"
    data = read_bin(path)
    print(data)
    
main()