from torch.autograd import Function
import torch 

class MyAdd(Function):
    
    @staticmethod
    def forward(ctx, input1, input2):
        return input1 + input2
    
    @staticmethod
    def backward(ctx, grad_outputs):
        grad_input1 = grad_outputs * 1
        grad_input2 = grad_outputs * 1
        
        return grad_input1, grad_input2
    
def custom_add(x1, x2):
    return MyAdd().apply(x1, x2)

def add(x1, x2):
    return torch.add(x1, x2)


if __name__ == "__main__":    
    print(5 * "==" + " Using PyTroch " + 5 * "==")
    x1_1 = torch.tensor([2.0], requires_grad=True)
    x1_2 = torch.tensor([3.0], requires_grad=True)
    y = add(2 * x1_1, x1_2**2)
    y.backward()
    print(f"y: {y}, \ngrad_x1: {x1_1.grad}, \ngrad_x2: {x1_2.grad}")

    print(5 * "==" + " Custom function " + 5 * "==")
    x2_1 = torch.tensor([2.0], requires_grad=True)
    x2_2 = torch.tensor([3.0], requires_grad=True)
    y2 = custom_add(2 * x2_1, x2_2**2) 

    y2.backward()
    print(f"y2: {y2}, \ngrad_x1: {x2_1.grad}, \ngrad_x2: {x2_2.grad}")
   