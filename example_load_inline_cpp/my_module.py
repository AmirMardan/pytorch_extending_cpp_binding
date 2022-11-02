# export CXX=/usr/local/opt/llvm/bin/clang

from torch.utils.cpp_extension import load_inline
import torch 


source = """ 
#include <torch/script.h>

    at::Tensor sin_add(at::Tensor x, at::Tensor y){
        return x.sin() + y.sin();
    }
    
    at::Tensor add(at::Tensor x, at::Tensor y){
        return x + y;
    }

TORCH_LIBRARY(my_op, m) {
  m.def("sin_add", &sin_add);
  m.def("add", &add);
}
"""

module = load_inline(name="my_op",
                    cpp_sources=[source],
                    is_python_module=False,
                    verbose=True
                    )
add = torch.ops.my_op.add

if __name__ == "__main__":
    x = add(2, 3)
    print(f"x: {x}")
    print(torch.ops.my_op.sin_add)