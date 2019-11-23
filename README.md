# DataContainer

[TOC]

把数据读到内存中，reload处理数据代码，反复调用数据。目的是保持数据在内存中，同时修改代码，避免反复从硬盘读取数据。

### 为什么有这种需求？

有时我们需要反复修改运行一个脚本，如果脚本每次运行都需要读取较大数据文件的话，就会浪费很多时间在读数据上。

比如进行金融数据的回测研究，需要不断修改回测逻辑，而反复读取数据是不必要的。

### 那么如何解决这个问题？

很自然的想到，把读数据和回测部分分开运行，因为需要修改的代码只有回测部分代码。

### 那么如何分开运行？

最简单的办法时使用jupyter运行代码片段。

### 如果不想使用jupyter，有其他方法吗？

有。使用多进程和reload，在主进程将数据读到内存，把回测逻辑写到单独的模块中。每次修改回测代码后，在主函数通过reload重读回测模块，把数据传进去，在子进程中运行回测（或者不使用多进程也可以）。

### 代码

基于上述原理，构建一个类来实现功能。原理很简单，实例化时，将数据和回测模块传入类

```python

# read_data.py

from importlib import reload  # python3 的reload函数在imp或importlib模块中
from multiprocessing import Process


class DataContainer(object):
    """数据容器，在内存中存储数据，供其他函数调用
    data: 数据
    module: 回测模块。模块必须含有main函数，并接收data参数
    """

    def __init__(self, data, module):
        super(DataContainer, self).__init__()
        self.data = data
        self.module = module

    def run(self):
        while True:
            try:
                cmd = input('# ')
                if cmd in ('run', 'r', 'c'):  # 输入'run', 'r', 'c'开始运行回测
                    reload(self.module)
                    Process(target=self.module.main,
                            args=(self.data, )).start()
            except Exception as e:
                print(e)
                continue

def main():
    data = 'data'  # 读取数据
    import backtest
    DataContainer(data=data, module=backtest).run()  # 输入'run', 'r', 'c'开始运行回测


if __name__ == '__main__':
    main()

```

```python
# backtest.py

# 回测逻辑
def main(data):
    print(data)
    pass


```

### 运行

每次修改backtest.py中的代码，然后在主进程中输入'r'运行。

