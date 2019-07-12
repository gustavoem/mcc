from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
import numpy

extensions = [
        Extension("c_odes", ["c_odes_wrapper.pyx"],
        include_dirs=[".", numpy.get_include()],
        library_dirs=["."])
]


setup(name="myapp",
    ext_modules=cythonize(extensions)
)
