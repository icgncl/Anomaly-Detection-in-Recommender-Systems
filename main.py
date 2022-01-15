from pyspark.sql import SparkSession
from core import Analysis


def main():
    # Initialize Spark
    spark = SparkSession.builder \
        .master("local[*]") \
        .appName("CENG790_Project") \
        .getOrCreate()

    # Read json and convert it to table
    magazine_df = spark.read.json('data/Magazine_Subscriptions.json')
    magazine_df.createOrReplaceTempView("magazine_table")

    # Calculating number of ratings per rating
    Analysis.number_of_ratings_per_rating(spark)

    # Calculating number of ratings per rating and year
    Analysis.number_of_ratings_per_rating_n_year(spark)

    # Calculating the totals on the data
    Analysis.calculate_totals(spark)




    spark.stop()


if __name__ == "__main__":
    main()
