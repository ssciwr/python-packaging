import random
import click


@click.command()
def flip_coin():
    return random.choice(["Heads", "Tails"])
