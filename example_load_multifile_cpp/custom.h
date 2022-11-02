#include <torch/script.h>
#include <iostream>

using torch::autograd::tensor_list;
using torch::autograd::AutogradContext;

class MyAdd : public torch::autograd::Function<MyAdd>{
    public:
    static at::Tensor forward(AutogradContext *ctx, at::Tensor input1, at::Tensor input2);
    static tensor_list backward(AutogradContext *ctx, tensor_list grad_outputs);
};