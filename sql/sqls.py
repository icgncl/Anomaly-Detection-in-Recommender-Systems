class SqlStrings:
    groupby_rating_sql = """
    SELECT overall, count(*) 
    FROM magazine_table
    GROUP BY overall
    ORDER BY overall
    """

    groupby_rating_time_sql = """
    WITH total_ratings_per_year as
    (SELECT YEAR(FROM_UNIXTIME(unixReviewTime)) as year,COUNT(*) as count_of_total_reviews
     FROM magazine_table
     GROUP BY YEAR(FROM_UNIXTIME(unixReviewTime))
     ORDER BY YEAR(FROM_UNIXTIME(unixReviewTime))
    ),
    total_ratings_per_year_w_ranks as
    (SELECT YEAR(FROM_UNIXTIME(mt.unixReviewTime)) as year, mt.overall, count(*) as per_rank_year
    FROM magazine_table as mt 
    GROUP BY YEAR(FROM_UNIXTIME(mt.unixReviewTime)), mt.overall
    ORDER BY YEAR(FROM_UNIXTIME(mt.unixReviewTime)), mt.overall
    )
    SELECT ty.year, tyr.overall, per_rank_year/count_of_total_reviews as rank_percentage 
    FROM total_ratings_per_year as ty LEFT JOIN total_ratings_per_year_w_ranks tyr ON ty.year = tyr.year
    ORDER BY ty.year, tyr.overall
    """

    totals = """
    SELECT 
        COUNT(*) as number_of_reviews, 
        COUNT(DISTINCT reviewerID) as total_number_of_users,
        COUNT(DISTINCT asin) as number_of_distinct_products,
        COUNT(CASE when reviewText is null then 1 END) as number_of_null_results
    FROM magazine_table
    """