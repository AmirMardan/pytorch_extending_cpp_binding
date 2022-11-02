// export CXX=/usr/local/opt/llvm/bin/clang

#include<pybind11/pybind11.h>
#include<iostream>
#include<vector>
#include <pybind11/stl.h>
#include<pybind11/complex.h>
#include<pybind11/functional.h>
#include<pybind11/chrono.h>
#include <pybind11/numpy.h>

namespace py = pybind11;


template<typename T>
T add(T a, T b){
    return a + b;
}

template <typename T>
std::vector<std::vector<T >> assign_special(std::vector<std::vector<T >> data){
    for(int i=0; i<2; i++){
        for (int c=0; c<2; c++){
            data[c][i] = 0.0;
        }
    }
    return data;
}


template <typename T>
void assign_special_ref(py::array_t<T> xs) {
    py::buffer_info info = xs.request();
    auto ptr = static_cast<double *>(info.ptr);
    
    int n = 1;
    for (auto r: info.shape) {
      n *= r;
    }

    for (int i = 0; i <n; i++) {
        *ptr++ *= 0;
    }
}

PYBIND11_MODULE(math_op, m){
    m.def("add", &add<int>);
    m.def("add", &add<double>);
    m.def("assign_special", &assign_special<double>);
    m.def("assign_special", &assign_special<int>);
    m.def("assign_special_ref", &assign_special_ref<float>);  // for np.float32
    m.def("assign_special_ref", &assign_special_ref<double>); // for np.float64
    m.def("assign_special_ref", &assign_special_ref<int>);  // for np.int32
}