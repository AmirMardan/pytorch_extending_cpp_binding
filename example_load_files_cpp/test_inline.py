""" 
This script is for testing the calling inline C++ function in Python
using PyTorch
"""
from my_module import add 

x = add(2, 4)
print(f"x: {x}")