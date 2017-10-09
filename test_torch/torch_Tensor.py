import torch
weights=torch.Tensor([0,10,3,0])
a=torch.multinomial(weights,4)
b=torch.multinomial(weights,4,replacement=True)
#print(a,b)
c=torch.normal(means=torch.arange(1,11),std=torch.arange(1,0,-0.1))
print(c)


