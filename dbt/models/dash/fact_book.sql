{{
    config(
        materialized='table'
    )
}}

with overview_data as(
    select * from {{ ref('stg_staging__overview') }}
),

review_data as(
    select * from {{ ref('stg_staging__book_review') }}
)

select *
from overview_data o left join review_data r on o.primary_isbn13 = r.review_book_isbn13