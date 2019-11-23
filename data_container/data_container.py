# -*- coding: utf-8 -*-

from importlib import reload
from multiprocessing import Process


class DataContainer(object):
    """数据容器，在内存中存储数据，供其他函数调用"""

    def __init__(self, data, module):
        super(DataContainer, self).__init__()
        self.data = data
        self.module = module

    def run(self):
        while True:
            try:
                cmd = input('# ')
                if cmd in ('run', 'r', 'c'):
                    reload(self.module)
                    Process(target=self.module.main, args=(self.data, )).start()
            except Exception as e:
                print(e)
                continue
