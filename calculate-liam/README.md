# calculate-liam

A simple example of a Python package from the [SSC Python Packaging course](https://ssciwr.github.io/python-packaging).

## testPyPI install

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

```bash
$ flip-coin
Tails
$ roll-dice --n-dice=2 --n-sides=12

 8

 5

```
