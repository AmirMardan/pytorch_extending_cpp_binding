from torch.utils.cpp_extension import load 
import os 
import torch

path = os.path.abspath(os.path.join(__file__, ".."))
    
sources = [path + "/my_module.cpp",
           path + "/custom_functions.cpp"]
print(sources)
module = load(name="multifile",
              sources=sources,
              is_python_module=False,
              verbose=True
              )

add = torch.ops.multifile.add
custom_add = torch.ops.multifile.my_add

if __name__ == "__main__":
    x1_1 = torch.tensor([2.0], requires_grad=True)
    x1_2 = torch.tensor([3.0], requires_grad=True)
    y = add(2 * x1_1, x1_2**2)
    
    x2_1 = torch.tensor([2.0], requires_grad=True)
    x2_2 = torch.tensor([3.0], requires_grad=True)
    y2 = custom_add(2 * x2_1, x2_2**2)
    
    y.backward()
    y2.backward()
    print(f"y: {y}, \ngrad_x1: {x1_1.grad}, \ngrad_x2: {x2_2.grad}")
    print(f"y2: {y2}, \ngrad_x1: {x2_1.grad}, \ngrad_x2: {x2_2.grad}")
    