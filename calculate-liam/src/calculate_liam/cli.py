import click
from .stats import flip_coin
from .stats import roll_dice


@click.command()
def flip_coin_cli():
    click.echo(flip_coin())


@click.command()
@click.option(
    "-d", "--n-dice", default=1, show_default=True, help="Number of dice to roll"
)
@click.option("-s", "--n-sides", default=6, show_default=True, help="Number of sides")
def roll_dice_cli(n_dice, n_sides):
    click.echo("")
    for d in roll_dice(n_dice, n_sides):
        click.secho(f" {d} ", bold=True, bg="red")
        click.echo("")
