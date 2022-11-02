#include "custom.h"

at::Tensor MyAdd::forward(AutogradContext *ctx, at::Tensor input1, at::Tensor input2){
    at::Tensor res = input1 + input2;
    ctx->save_for_backward({input1, input2});

    return res;
}

tensor_list MyAdd::backward(AutogradContext *ctx, tensor_list grad_outputs){
    auto saved = ctx -> get_saved_variables();
    auto input1 = saved[0];
    auto input2 = saved[1];

    auto grad_output = grad_outputs[0];
        
    auto grad_input1 = grad_output * torch::tensor({1});
    auto grad_input2 = grad_output * torch::tensor({1});
    return {grad_input1, grad_input2};
}