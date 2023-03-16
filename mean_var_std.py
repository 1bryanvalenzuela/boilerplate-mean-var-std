#!/usr/bin/env python
# coding: utf-8

import numpy as np
import pandas as pd

def calculate(nums):
    try:
        tt1 = np.array(nums)
        tt2 = tt1.reshape(3,3)
        return {
        'mean': [np.round(tt2.mean(axis=0),2).tolist(),np.round(tt2.mean(axis=1),2).tolist(),np.round(tt2.mean(),2).tolist()],
        'variance': [np.round(tt2.var(axis=0),2).tolist(),np.round(tt2.var(axis=1),2).tolist(),np.round(tt2.var(),2).tolist()],
        'standard deviation': [np.round(tt2.std(axis=0),2).tolist(),np.round(tt2.std(axis=1),2).tolist(),np.round(tt2.std(),2).tolist()],
        'max': [np.round(tt2.max(axis=0),2).tolist(),np.round(tt2.max(axis=1),2).tolist(),np.round(tt2.max(),2).tolist()],
        'min': [np.round(tt2.min(axis=0),2).tolist(),np.round(tt2.min(axis=1),2).tolist(),np.round(tt2.min(),2).tolist()],
        'sum': [np.round(tt2.sum(axis=0),2).tolist(),np.round(tt2.sum(axis=1),2).tolist(),np.round(tt2.sum(),2).tolist()],
        }
    except ValueError:
        print("ValueError: List must contain nine numbers")

