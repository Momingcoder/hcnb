#!/usr/bin/env python
# coding=utf-8

import pickle
import os

def u(x):
    if not isinstance(x, unicode):
        return x.decode('utf-8')
    return x

def file2list(f):
    if not isinstance(f, str):
        raise TypeError
    listr = []
    with open(f, 'r') as ff:
        for line in ff.readlines():
            listr.append(u(line.strip()))
    return listr

class HachiFilter(object):
    """
    The basic class for Hachi filters.
    """
    def __init__(self, arg={}):
        self.arg = arg
        self.filter = object()
        self.load_model()

    def load_model(self):
        filepath = self.__name__ + '.pickle'
        if not os.path.exists(filepath):
            self.fit()
            with open(filepath, 'wb') as fw:
                pickle.dump(self.filter, fw)
                fw.close()
        else:
            with open(filepath, 'rb') as fr:
                self.filter = pickle.load(fr)
                fr.close()

    def predict(self, message, level=0):
        return self.filter.predict(message)

    def reset_param(self, arg):
        self.arg = arg
        self.load_model()
