import pyximport
pyximport.install()
from .primes import primes
from .engine import Value 

__version__ = "0.0.6"
