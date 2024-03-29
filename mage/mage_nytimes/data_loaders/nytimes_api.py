import io
import pandas as pd
import requests
from mage_ai.data_preparation.shared.secrets import get_secret_value

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """
    url = 'https://api.nytimes.com/svc/books/v3/lists/full-overview.json?api-key='+get_secret_value('api_key')
    response = requests.get(url)
    data = response.json()

    lists_data = data.get('results', {})
    return lists_data
    

@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
