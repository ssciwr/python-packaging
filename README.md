# [Python Packaging](https://ssciwr.github.io/python-packaging)

[![SSC Compact Course](https://img.shields.io/badge/SSC-Compact_Course-blue?style=flat&logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA0Mi4zNDc5MzkgNDIuMzQ4MTc1Ij4KICA8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgtMzMuOTc4NzE5LC0zOC44NDg5MikiPgogICAgPHBhdGggZD0ibSAzMy45Nzg4OTMsNDMuODEyODU3IGMgMCwtMi43NDE0MzcgMi4yMjIzNjEsLTQuOTYzOTM3IDQuOTYzOTczLC00Ljk2MzkzNyBoIDMyLjQxOTg1NyBjIDIuNzQxNDM2LDAgNC45NjM5MzYsMi4yMjI1IDQuOTYzOTM2LDQuOTYzOTM3IHYgMzIuNDE5ODU2IGMgMCwyLjc0MTYwNiAtMi4yMjI1LDQuOTY0MTA2IC00Ljk2MzkzNiw0Ljk2NDEwNiBIIDM4Ljk0Mjg2NiBjIC0yLjc0MTYxMiwwIC00Ljk2Mzk3MywtMi4yMjI1IC00Ljk2Mzk3MywtNC45NjQxMDYgViA0My44MTI4NTciIHN0eWxlPSJmaWxsOiNmZmZmZmY7ZmlsbC1vcGFjaXR5OjE7ZmlsbC1ydWxlOm5vbnplcm87c3Ryb2tlOm5vbmUiLz4KICAgIDxwYXRoIGQ9Im0gNDkuNDM2NjMsNTcuNjUzODQ3IGMgMCwxLjc4ODU4MyAtMC42Njk0NjYsMy40MjA1NjggLTEuNzcxMzMyLDQuNjU5NDU0IC0yLjk2MDcyMywwLjY2NTAyMSAtNS44MzQ2MjgsLTAuMjc5MDgzIC03LjcyMzUwNiwtMS44NTg3MTYgLTEuOTM5OTk2LC0xLjYyMjQ5NiAtMy4wNjg3NDMsLTMuOTI2NzM1IC0zLjIzODY1NSwtNi44NjAyOTQgMS4yNzExMDcsLTEuNzg3NTk1IDMuMzU5Mzc2LC0yLjk1MzgwOCA1LjcxOTk1MywtMi45NTM4MDggMy44NzM1MzYsMCA3LjAxMzU0LDMuMTM5ODYzIDcuMDEzNTQsNy4wMTMzNjQiIHN0eWxlPSJmaWxsOiM0MGI5NDUiLz4KICAgIDxwYXRoIGQ9Im0gNjUuNzYyNzk5LDYzLjQzODg3MyBjIDIuNjg4NDEzLC0wLjMxMjgwOCA1LjQ4MjgwMiwwLjYzODE3NSA3LjQzMTU0NiwyLjgwMjkyNiAzLjE5NDc1NiwzLjU0ODczMyAyLjkwODMsOS4wMTUxMzEgLTAuNjQwMjkxLDEyLjIwOTgzIC0xLjY0MjE4MSwxLjQ3ODYzNiAtMy42OTUyMDcsMi4yMTE2MTMgLTUuNzQzODIzLDIuMjIwMjk1IC0zLjA0ODA3LC0yLjE2NDA2OSAtNC41NTIwNjgsLTUuNTczNjAzIC00LjY2MjczNCwtOC42MDU0NDYgLTAuMTEzOTQ4LC0zLjExNjU0NSAxLjA2NjYyMywtNi4wNTE5MDMgMy42MTUzMDIsLTguNjI3NjA1IiBzdHlsZT0iZmlsbDojZWUyMzI3Ii8%2BCiAgICA8cGF0aCBkPSJtIDY3Ljc0NDk1MSw1MC4xMDgyODIgYyAtMC41OTM5MzYsMS4xMTcwMzYgLTEuNTU3MTYxLDEuOTExMjA5IC0yLjY1OTMwOSwyLjMxMTkzIC0yLjA0Njk1OCwtMC41NjU1MzggLTMuNTExNzk3LC0yLjA5NDA1NCAtNC4xNjA0NSwtMy42OTE2NDQgLTAuNjY3NTI2LC0xLjY0NDgyNiAtMC42MDczMDcsLTMuNDQ0NjI4IDAuMjU1MDU4LC01LjMxODIzMSAxLjM3ODYyMSwtMC42OTYzODMgMy4wNjMyNDEsLTAuNzM0MTMgNC41MzA3MjYsMC4wNDY1NyAyLjM5ODIxOCwxLjI3NTY0NCAzLjMwODgwOCw0LjI1MzQ0MiAyLjAzMzk3NSw2LjY1MTM3OCIgc3R5bGU9ImZpbGw6I2JkMjI5OCIvPgogICAgPHBhdGggZD0ibSA1OC43NDExNDUsNTMuMzU0MjYxIGMgLTMuMDY4NjM4LC0yLjU3NDMyNSAtMy40NjkyMTcsLTcuMTQ4NTEzIC0wLjg5NDc1MSwtMTAuMjE2OTc0IDIuNTc0NDMyLC0zLjA2ODQ2MSA3LjE0ODk3MiwtMy40Njg1MTEgMTAuMjE3NTc0LC0wLjg5NDI5MiAzLjA2ODc0NCwyLjU3NDU3MyAzLjQ2OTE0Nyw3LjE0ODU0OSAwLjg5NDc4NiwxMC4yMTY5MDQgLTIuNTc0NDY3LDMuMDY4MzU2IC03LjE0OTAwNywzLjQ2ODY1MyAtMTAuMjE3NjA5LDAuODk0MzYyIHogTSAzMy45Nzg4OTMsNDMuODEyODU3IGMgMCwtMi43NDE0MzcgMi4yMjIzNjEsLTQuOTYzOTM3IDQuOTYzOTczLC00Ljk2MzkzNyBoIDMyLjQxOTg1NyBjIDIuNzQxNDM2LDAgNC45NjM5MzYsMi4yMjI1IDQuOTYzOTM2LDQuOTYzOTM3IGwgLTAuMDAxOCwyMC4wNDU2MSBjIC0yLjMwNTA1LC0yLjY4Nzg0OSAtNS43MzA1MjIsLTQuMzk2NjM0IC05LjU1NTE2MywtNC4zOTY2MzQgLTYuOTM5MjQ1LDAgLTEyLjU2NDM5Myw1LjYyNTI4OSAtMTIuNTY0MzkzLDEyLjU2NDU2OSAwLDMuNjE3NTk2IDEuNTI4OTA0LDYuODc4MTg3IDMuOTc1NzcxLDkuMTcwNjkyIEwgMzguOTQyODMsODEuMTk2ODE5IGMgLTIuNzQxNjEyLDAgLTQuOTYzOTczLC0yLjIyMjUgLTQuOTYzOTczLC00Ljk2NDEwNiBsIC0xLjM4ZS00LC0xMi41NTUwNDQgYyAwLjUwMDIyNywwLjcwMjM4IDEuMDk2NzgxLDEuMzUzNTM4IDEuNzg4MTQxLDEuOTMzNTQgNC4zODcxMjcsMy42ODA3NDIgMTAuOTI3NDE2LDMuMTA4MTQ4IDE0LjYwODI5OSwtMS4yNzg4MiAzLjY4MTAyNSwtNC4zODcxMDkgMy4xMDg1NzMsLTEwLjkyNzI5MiAtMS4yNzg1MzcsLTE0LjYwODAzNSAtNC4zODcxMDksLTMuNjgwODgzIC0xMC45Mjc0MzMsLTMuMTA4MTQ5IC0xNC42MDg0NDQsMS4yNzg4MiAtMC4xNzk5NjksMC4yMTQ1NTkgLTAuMzQ5NzQ0LDAuNDM0MjM0IC0wLjUwOTQ1OSwwLjY1ODQyNCBsIDEuMzhlLTQsLTcuODQ4NzQxIiBzdHlsZT0iZmlsbDojM2E5ZWJmO2ZpbGwtcnVsZTpldmVub2RkIi8%2BCiAgPC9nPgo8L3N2Zz4K&labelColor=%23ffffff&color=%233a9ebf)](https://www.ssc.uni-heidelberg.de/en/learning)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> In this course we will learn how to package a Python library, how to publish it on PyPI and on conda-forge, as well as look at more advanced topics like building pre-compiled wheels including c++ extensions using pybind11, and automatically publishing new releases using continuous integration and cibuildwheel.

This repo contains example source code for the SSC compact course ["Python Packaging"](https://www.ssc.uni-heidelberg.de/en/compact-course-python-packaging).

## Slides

[![Course slides](https://ssciwr.github.io/python-packaging/slides-thumb.png)](https://ssciwr.github.io/python-packaging)

[Open slides](https://ssciwr.github.io/python-packaging) | [Download as PDF](https://ssciwr.github.io/python-packaging/slides.pdf)

## Python Package Examples

### Pure Python Package

- [calculate-minimal](https://github.com/ssciwr/python-packaging/tree/main/calculate-minimal)
  - A bare-bones minimal Python package that can be locally installed
- [calculate-liam](https://github.com/ssciwr/python-packaging/tree/main/calculate-liam)
  - A more complete version of this Python package that is [published on testPyPI](https://test.pypi.org/project/calculate-liam)
  - This [github action](https://github.com/ssciwr/python-packaging/blob/main/.github/workflows/pypi.yml) automatically publishes new versions to testPyPI on tagged commits

### Python Package with C++ compiled extensions

- [pybind11-numpy-example](https://github.com/ssciwr/pybind11-numpy-example)
  - a simple example of packaging including c++ compiled extensions
  - an example [meta.yaml](https://github.com/conda-forge/staged-recipes/pull/25040/files) conda-forge recipe for this package
  - the resulting [conda-forge feedstock](https://github.com/conda-forge/pybind11-numpy-example-feedstock) for this package
- [hammingdist](https://github.com/ssciwr/hammingdist)
  - a more advanced example with a compiled extension making use of OpenMP and CUDA

## Recommended resources

- Pure Python packaging
  - [Python Packaging Tutorial](https://packaging.python.org/en/latest/tutorials/packaging-projects)
  - [Scientific Python Simple packaging](https://learn.scientific-python.org/development/guides/packaging-simple)
- Python packaging with compiled extensions
  - [Scientific Python Compiled packaging](https://learn.scientific-python.org/development/guides/packaging-compiled)
  - [scikit-build-core getting started](https://scikit-build-core.readthedocs.io/en/latest/getting_started.html)
  - [pypackaging-native](https://pypackaging-native.github.io/)
- Cookiecutters to generate your own GitHub repo for a Python package
  - [ssciwr/cookiecutter-python-package](https://github.com/ssciwr/cookiecutter-python-package)
  - [scientific-python/cookie](https://github.com/scientific-python/cookie)
