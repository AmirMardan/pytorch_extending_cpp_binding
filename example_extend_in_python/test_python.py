""" 
This script is for testing the defined custom summation function in 
Pyhton. 
"""
from my_module import add, custom_add
import torch 

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
    