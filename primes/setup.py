from setuptools import setup, Extension
from Cython.Build import cythonize

extensions = [
    Extension("primes", ["../primes/primes.pyx"])
]

setup(
    name="primes",
    ext_modules=cythonize(extensions)
)