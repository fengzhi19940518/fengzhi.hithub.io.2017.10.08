import torch
from torch.autograd import  Variable
import torch.nn as nn

class Test(nn.Module):
    def __init__(self):
        super(Test,self).__init__()
        self.conv2=nn.Linear(1,2)
        self.vari=Variable(torch.rand([1]))
        self.par=nn.Parameter(torch.rand([1]))
        self.register_buffer("buffer",torch.randn([2,3]))

t=Test()
print(t.state_dict().keys())
