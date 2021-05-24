import click
import requests
import sseclient

store_url = "http://localhost:5002/kvstore"


@click.command()
@click.argument('given_key', default='sample_key', required=True)
def get(given_key):
    """GET request option, pass key as argument"""
    response = requests.get(store_url, params={"key": given_key})
    click.echo(response.text)


@click.command()
@click.argument('given_key', default='sample_key', required=True)
@click.argument('given_value', default='sample_value', required=True)
def put(given_key, given_value):
    """PUT request option, pass key, value as arguments"""
    response = requests.post(
        store_url, data={'key': given_key, 'value': given_value})
    # click.echo(response.text)


@click.command()
@click.argument('given_key', default='sample_key', required=True)
def watch(given_key):
    """PUT request option, pass key, value as arguments"""
    messages = sseclient.SSEClient(
        'http://localhost:5002/listen?key='+given_key)
    for msg in messages:
        print("The key {} has been {}".format(msg.event, msg.data))
