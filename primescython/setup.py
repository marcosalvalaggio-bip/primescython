from setuptools import setup, Extension
from Cython.Build import cythonize
from sys import platform

extensions = [
    Extension("primes", ["../primescython/primes.pyx"])
]

setup(
        name="primes-mac",
        ext_modules=cythonize(extensions)
    )



