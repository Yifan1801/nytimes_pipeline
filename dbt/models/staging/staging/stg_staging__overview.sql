with 

source as (

    select * from {{ source('staging','overview') }}

),

renamed as (

    select
        author,
        contributor,
        cast(created_date as timestamp) as created_date,
        description,
        primary_isbn10,
        primary_isbn13,
        publisher,
        rank,
        rank_last_week,
        title,
        cast(updated_date as timestamp) as updated_date,
        weeks_on_list,
        cast(list_id as string) as list_id,
        list_name,
        updated,
        cast(published_date as date) as published_date

    from source

)

select * from renamed
