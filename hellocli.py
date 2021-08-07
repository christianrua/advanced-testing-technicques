#!/usr/bin/env python
import click
from hello import addThis


@click.command()
@click.option('--x', required=True,type=int,help="Firts number to add" )
@click.option('--y', required=True,type=int,help="Second number to add")
def calladdthis(x,y):
    "This is a CLI that adds x, y"
    result = addThis(x,y)
    click.echo(click.style(f'{result}', bg='red'))


if __name__ == '__main__':
    #pylint: disable=no-value-for-parameter
    calladdthis()