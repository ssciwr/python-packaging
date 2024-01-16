import pytest
import numpy as np
from calculate import stats


def test_flip_coin():
    coin = stats.flip_coin()
    assert coin in ["Heads", "Tails"]


@pytest.mark.parametrize("n_dice", [1, 2, 5, 17])
@pytest.mark.parametrize("n_sides", [2, 3, 6, 20])
def test_roll_dice(n_dice, n_sides):
    dice = stats.roll_dice(n_dice, n_sides)
    assert len(dice) == n_dice
    assert np.all(dice >= 1)
    assert np.all(dice <= n_sides)
