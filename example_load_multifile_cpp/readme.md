Extending Torch in C++
============================

In this folder, I show how to add new functions to `autograd`. 

For this purpose, we create a class with a new [`Function`](https://pytorch.org/docs/stable/autograd.html#torch.autograd.Function) subclass and two static methods as called forward and backward as 
```C++
class NewOperator : public torch::autograd::Function<NewOperator>{
    public:
    static at::Tensor forward(AutogradContext *ctx, at::Tensor inputs){
        ...
        return outputs;
    }
    static tensor_list backward(AutogradContext *ctx, tensor_list grad_outputs){
        ...
        return grads
    }
};

```

Then, we create a function to call this class using method `apply` as
```C++
Tensor my_add(at::Tensor inputs){
    return NewOperator::apply(inputs)
```




Reference
==========
- [AUTOGRAD IN C++ FRONTEND](https://pytorch.org/tutorials/advanced/cpp_autograd.html)