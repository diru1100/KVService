import pytest


@pytest.fixture(scope="module")
def test_data():
    return {"key": "test_key", "value": "test_value",
            "get_output_template": '"Fetched details are {} : {}"\n',
            "post_output_template": '"Successfully {} key: {}, value: {}"\n',
            "store_url": "http://localhost:5002/kvstore"}
