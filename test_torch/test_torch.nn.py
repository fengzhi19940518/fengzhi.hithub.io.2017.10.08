import torch.nn as nn
import torch.nn.functional as F

# class Model(nn.Module):
#     def __init__(self):
#        # super(Model,self).__init__()
#         #self.conv1=nn.Conv2d(1,20,5)  #subModule:conv2d
#         sub_module=nn.Conv2d(20,20,5)
#         self.add_module("conv",sub_module)
#         self.add_module('conv2',sub_module)
#
# model=Model()
# for sub_module in model.modules():
#     print(sub_module)

class Model(nn.Module):
    def __init__(self):
        super(Model,self).__init__()

