import random
import numpy as np


def flip_coin() -> str:
    return random.choice(["Heads", "Tails"])


def roll_dice(n_dice: int, n_sides: int):
    return np.random.randint(low=1, high=n_sides + 1, size=n_dice)
