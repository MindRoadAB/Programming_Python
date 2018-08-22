#The cythonize function is used to convert Cython source to 
#C source code by calling the cython compiler.

from distutils.core import setup
from Cython.Build import cythonize

#To generate annotate HTML-file you need to:
# 1- import subprocess
# 2- Activate the annotate flag to <True>
#That's will produce a HTML file with yellow shading to show Python vs C code
import subprocess
subprocess.call(["cython","-a","example_py.pyx"])

ext_options = {"compiler_directives": {"profile": True}, "annotate": True}
exts = cythonize('example_py.pyx', **ext_options)


setup(
    ext_modules = exts, requires=['pytest']
)