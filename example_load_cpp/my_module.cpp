#include "custom.h"

using at::Tensor;

at::Tensor sin_add(at::Tensor x, at::Tensor y){
    return x.sin() + y.sin();
}
    
at::Tensor add(at::Tensor x, at::Tensor y){
    return x + y;
}


Tensor my_add(at::Tensor x, at::Tensor y){

    Tensor res = MyAdd::apply(x, y);
    return res;
}

TORCH_LIBRARY(multifile, m) {
  m.def("sin_add", &sin_add);
  m.def("add", &add);
  m.def("my_add", &my_add);
}