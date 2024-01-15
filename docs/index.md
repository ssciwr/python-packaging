## Description

In this course we will learn how to package a Python library, how to publish it on PyPI and on conda-forge, as well as look at more advanced topics like building pre-compiled wheels including c++ extensions using pybind11, and automatically publishing new releases using continuous integration and cibuildwheel.

## Slides

<iframe src="https://docs.google.com/presentation/d/e/2PACX-1vT_Vn29jIR56s5mhC05Gasn3krbcw89fmG9TFEDn4Etmd5VhswnmdA0A8v5Z1aVqpvJtiUuvJSn7GDZ/embed?start=false&loop=false&delayms=3000" frameborder="0" width="960" height="569" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>

[download slides as pdf](https://github.com/ssciwr/effective-software-testing/raw/main/docs/slides/slides.pdf) | [course description](https://www.ssc.uni-heidelberg.de/en/compact-course-python-packaging)

## Python Package Examples

### Pure Python Package

- [calculate-minimal](https://github.com/ssciwr/python-packaging/tree/main/calculate-minimal)
  - A bare-bones minimal Python package that can be locally installed
- [calculate](https://github.com/ssciwr/python-packaging/tree/main/calculate)
  - A better version of this Python package that can be published to PyPI

### Python Package with C++ compiled extensions

- [pybind11-numpy-example](https://github.com/ssciwr/pybind11-numpy-example)
  - a simple example of packaging including c++ compiled extensions
- [hammingdist](https://github.com/ssciwr/hammingdist)
  - a more advanced example with a compiled extension making use of OpenMP and CUDA

## Recommended resources

- Pure Python packaging
  - [Python Packaging Tutorial](https://packaging.python.org/en/latest/tutorials/packaging-projects)
  - [Scientific Python Simple packaging](https://learn.scientific-python.org/development/guides/packaging-simple)
- Python packaging with compiled extensions
  - [Scientific Python Compiled packaging](https://learn.scientific-python.org/development/guides/packaging-compiled)
  - [scikit-build-core getting started](https://scikit-build-core.readthedocs.io/en/latest/getting_started.html)
- Cookiecutters to generate your own GitHub repo for a Python package
  - [ssciwr/cookiecutter-python-package](https://github.com/ssciwr/cookiecutter-python-package)
  - [scientific-python/cookie](https://github.com/scientific-python/cookie)
