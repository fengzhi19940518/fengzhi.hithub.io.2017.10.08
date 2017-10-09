import torch
from numpy import *

class Test:
    def test(self):
        cent=zeros((3,5))       #zeros(m,n)产生m×n的double类零矩阵，zeros(n)产生n×n的全0方阵
        print('cent=',type(cent[:,2]))
        x=random.rand(2,10)     #.rand(m,n)或rand([m n])产生m×n均匀分布的随机矩阵，元素取值在0.0~1.0。
        print('x=',type(x))

        cent = zeros((3,4,5))
        print('shape',shape(cent)[1])   #shape函数是numpy.core.fromnumeric中的函数，它的功能是读取矩阵的长度
        r=torch.randn(3,4)
        print(r)
        print(r[:,2])   #打印第三列
        print(r[1,:])   #打印第二行
        #r=randn(3,4)        #randn()返回一个m*n的随机项矩阵。
test=Test()
test.test()