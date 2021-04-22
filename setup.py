"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# To use a consistent encoding
from codecs import open
from os import path, environ

# Always prefer setuptools over distutils
from setuptools import setup

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
      name='python-cfonb',
      
      version='2.9',
      
      description="Pure Python lib to read/write CFONB files, forked from https://github.com/akretion/python-cfonb",
      long_description=long_description,
      
      classifiers=[],
      keywords=['cfonb', 'bank', 'statement', 'parser'],
      
      author='Dhatim',
      author_email='contact@dhatim.com',
      
      url='https://github.com/dhatim/python-cfonb',
      
      license='LGPL',
      packages=['python-cfonb'],
      python_requires='>=2.7',
	  install_requires=['semantic_version>=2.7.0', 'toml'],
      
      entry_points={
        'console_scripts': [
            'python-cfonb=python-cfonb.command_line:main'
        ],
    },
)
