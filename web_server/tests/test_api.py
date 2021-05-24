import pytest
import requests
import sseclient

# from ..api.resources import store, listen


def test_store_resource_get_request(test_data):

    test_key = test_data["key"]
    test_value = test_data["value"]
    store_url = test_data["store_url"]

    response = requests.post(
        store_url, data={'key': test_key, 'value': test_value})

    response = requests.get(store_url, params={"key": test_key})

    assert(200 == response.status_code)
    assert(test_data["get_output_template"].format(
        test_key, test_value) == response.text)

    # deleting test data
    requests.delete(store_url, params={"key": test_key})


def test_store_resource_post_request(test_data):
    test_key = test_data["key"]
    test_value = test_data["value"]
    store_url = test_data["store_url"]

    response = requests.post(
        store_url, data={'key': test_key, 'value': test_value})

    assert(200 == response.status_code)
    assert(test_data["post_output_template"].format(
        "Stored !!", test_key, test_value) == response.text)

    response = requests.post(
        store_url, data={'key': test_key, 'value': test_value})

    assert 200 == response.status_code
    assert test_data["post_output_template"].format(
        "Updated !!", test_key, test_value) == response.text

    # deleting test data
    requests.delete(store_url, params={"key": test_key})
