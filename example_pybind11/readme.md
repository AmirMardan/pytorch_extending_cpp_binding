Manual compiling
================
For MacOS, we can manually compile the code using 
```bash
$ c++ -O3 -Wall -shared -std=c++11 -undefined dynamic_lookup $(python3 -m pybind11 --includes) math_op.cpp -o math_op$(python3-config --extension-suffix)
```

For installing the package, go to the directory with the file `setup.py` and run `pip install .`.
Then we can use file `wrap_test.py`. 
This file has three examples as
1. simple summation function `op.add(3, 2)`,
2. using a function to get ndarray with value as argument, `op.assign_special()`,
3. using a function to get ndarray with value as argument, `op.assign_special_ref().

References
===========
[Using pybind11](https://people.duke.edu/~ccc14/cspy/18G_C++_Python_pybind11.html)

