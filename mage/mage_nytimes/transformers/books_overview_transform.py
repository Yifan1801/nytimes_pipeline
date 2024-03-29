import pandas as pd

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    """
    Template code for a transformer block.

    Add more parameters to this function if this block has multiple parent blocks.
    There should be one parameter for each output variable from each parent block.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Specify your transformation logic here
    book_data = data.get('lists', {})
    published_date = data['published_date']

    df = pd.json_normalize(book_data,
                  record_path=['books'],
                  meta = ['list_id', 'list_name', 'updated'])

    df.drop(columns = ['age_group', 'amazon_product_url','article_chapter_link','book_image',
        'book_image_width','book_image_height','book_review_link','book_uri',
        'contributor_note','first_chapter_link','sunday_review_link','buy_links', 'price'
        ], inplace = True)
    
    df['published_date'] = published_date
    print(df)
    return df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
