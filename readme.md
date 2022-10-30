Extending Torch and binding C++ function
========================================

We can extend the autograd operation in both Python and C++ which is discussed in folders `example_extend_in_python` and `example_load_cpp`.

To bind C++ to Python, we can use just-in-time (JIT) method. 
For this purpose, we write our functions in C++ and at the end of the C++ file, we define the functions that need to be wrapped using pybind11 as 
```C++
TORCH_LIBRARY(module_name, m) {
  m.def("name_of_function_in_python", &name_of_function_in_cpp);  
}

```
Then, we load C++ files as 

```Python
from torch.utils.cpp_extension import load
module = load(
    name='module_name',
    sources=['source1.cpp',
    'source2.cu'],
     extra_cflags=['-O2'],
     verbose=True)
```
and now, we can call the created function as 
```Python
add = torch.ops.module_name.name_of_function_in_python
```

Reference
==========
- [Torch C++ Extension](https://pytorch.org/docs/stable/cpp_extension.html#torch-utils-cpp-extension)
