# calculate-liam

A simple example of a Python package from the [SSC Python Packaging course](https://ssciwr.github.io/python-packaging),
which is published on [testPyPI](https://test.pypi.org/project/calculate-liam/)

## install from testPyPI

First ensure that the dependencies are installed from (real) PyPI:

`pip install click numpy`

Then you can install this package from test PyPI:

`pip install -i https://test.pypi.org/simple/ calculate-liam`

## Python use

```python
from calculate_liam import stats

print(stats.flip_coin())

print(stats.roll_dice(n_dice=2, n_sides=12))
```

## Command line use

![CLI gif](https://raw.githubusercontent.com/ssciwr/python-packaging/main/calculate-liam/docs/cli.gif)

## automatic testPyPI publishing

Tagged commits are automatically published on testPyPI using [this github action](https://github.com/ssciwr/python-packaging/blob/main/.github/workflows/pypi.yml)

## conda-forge recipe

An example recipe that could be used to submit this package to conda-forge is [meta.yaml](https://github.com/ssciwr/python-packaging/blob/main/calculate-liam/meta.yaml)
