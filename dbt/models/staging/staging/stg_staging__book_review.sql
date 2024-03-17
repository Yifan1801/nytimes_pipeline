with 

source as (

    select * from {{ source('staging', 'book_review') }}

),

renamed as (

    select
        url as review_url,
        cast(publication_dt as date) as review_publication_dt,
        byline as review_byline,
        book_title as review_book_title,
        cast(book_author as string) as reviewed_book_author,
        summary as review_summary,
        cast(isbn13 as string) as review_book_isbn13

    from source

)

select * from renamed
