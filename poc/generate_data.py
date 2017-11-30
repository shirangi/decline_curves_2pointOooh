import numpy as np
import torch


def t0():
    a = torch.Tensor(3, 3).uniform_(0, 1)
    print(a)
    b = torch.Tensor([[1, 2], [3, 4]])
    print(b)
    b.zero_()
    print(b)
    b[0] = 2
    print(b)
    b[1][1] = 1
    print(b)
    b.sin_() # inplace
    print(b)
    a = b.asin()
    print(b)
    print(a)
    print(a.size())


if __name__ == '__main__':
    t0()
