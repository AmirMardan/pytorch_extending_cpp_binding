from glob import glob
from setuptools import setup
from pybind11.setup_helpers import Pybind11Extension
import os 

cpp_args = ['-std=c++11', '-stdlib=libc++', '-mmacosx-version-min=10.7']
name = "math_op"
version = "1.0"

path = os.path.abspath(os.path.join(__file__, ".."))
# print(path + "/math_op_template.cpp")
ext_modules = [
    Pybind11Extension(
        name,
        [path + "/math_op.cpp"], 
        include_dirs=['pybind11/include'],
        language='c++',
        extra_compile_args = cpp_args,
    ),
]

setup(name=name,
      version=version,
      author="Amir Mardan",
      author_email = "mardan.amir.h@gmail.com",
      description="Example",
      ext_modules=ext_modules)
