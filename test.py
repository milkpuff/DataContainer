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
    data = np.random.randn(100, 100)  # 假设这是从硬盘读到内存的数据
    print(data)
    DataContainer(data, main_test).run()  # 这里会重复调用data而不用重新从硬盘读取


if __name__ == '__main__':
    main()
