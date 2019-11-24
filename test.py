# -*- coding: utf-8 -*-

'''
'''
import os
import sys
import time
import datetime
import numpy as np
import pandas as pd

from data_container import DataContainer
import main_test


def main():
    data = np.random.randn(100, 100)
    print(data)
    DataContainer(data, main_test).run()


if __name__ == '__main__':
    main()
