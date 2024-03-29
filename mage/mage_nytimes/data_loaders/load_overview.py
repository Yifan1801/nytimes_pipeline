from mage_ai.settings.repo import get_repo_path
from mage_ai.io.config import ConfigFileLoader
from mage_ai.data_preparation.shared.secrets import get_secret_value
from mage_ai.io.google_cloud_storage import GoogleCloudStorage
from os import path
import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_from_google_cloud_storage(*args, **kwargs):
    """
    Template for loading data from a Google Cloud Storage bucket.
    Specify your configuration settings in 'io_config.yaml'.

    Docs: https://docs.mage.ai/design/data-loading#googlecloudstorage
    """
    config_path = path.join(get_repo_path(), 'io_config.yaml')
    config_profile = 'default'

    bucket_name = 'nytimes_project'
    object_key = 'best_seller_overview.csv'

    overview_data = GoogleCloudStorage.with_config(ConfigFileLoader(config_path, config_profile)).load(
        bucket_name,
        object_key,
    )
    #get isbn data
    isbn_data = overview_data[['primary_isbn13']].drop_duplicates().values
    api_key = "Zze3RLOu6uNAu6sjDGKAUtMIQX7exEiF"
    result = pd.DataFrame()

    for isbn in isbn_data:
        if not isbn:
            continue
        i_url = "https://api.nytimes.com/svc/books/v3/reviews.json?api-key="+ get_secret_value('api_key')+"&isbn="+str(isbn[0])

        response = requests.get(i_url)
        data = response.json()

        review_data = data.get('results', {})
        if review_data:
            df = pd.json_normalize(review_data)
            df = df[['url', 'publication_dt', 'byline', 'book_title', 'book_author', 'summary']]
            df['isbn13'] = str(isbn[0])
            result = pd.concat([result, df], ignore_index=True)

    return result


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
