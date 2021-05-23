import click
import requests

base_url = "http://localhost:5000/kvstore"


@click.command()
@click.argument('given_key', default='sample_key', required=True)
def get(given_key):
    """GET request option, pass key as argument"""
    response = requests.get(base_url, params={"key": given_key})
    click.echo(response.text)
    click.echo(response.status_code)


@click.command()
@click.argument('given_key', default='sample_key', required=True)
@click.argument('given_value', default='sample_value', required=True)
def put(given_key, given_value):
    """PUT request option, pass key, value as arguments"""
    response = requests.post(
        base_url, data={'key': given_key, 'value': given_value})
    click.echo(response.text)


@click.command()
@click.argument('given_key', default='sample_key', required=True)
def watch(given_key,):
    """PUT request option, pass key, value as arguments"""
    # TODO
