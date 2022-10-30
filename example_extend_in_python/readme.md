Extending PyTorch in Python
============================

In this folder, I show how to add new functions to `autograd`. 

For this purpose, we create a class with a new [`Function`](https://pytorch.org/docs/stable/autograd.html#torch.autograd.Function) subclass and two static methods called forward and backward as 
```Python
class NewOperator(nn.autograd.Function):
    @staticmethod
    def forward(ctx, inputs):
        ...
        return outputs
    
    @staticmethod
    def backward(ctx, grad_outputs):
        ...
        return grads

```

Then, we create a function to call this class using method `apply` as
```Python
def new_operator(inputs):
    return NewOperator().apply(inputs)
```




Reference
==========
- [PyTorch](https://pytorch.org/docs/stable/notes/extending.html)