import torch
from pyspark.sql import SparkSession
from core import Analysis
from model import Model


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

    # This function creates new csv from dataset
    # In the new csv, ratings were calculated according to their reviewTexts
    Model.create_new_data_w_nlp()

    # Anomaly Detection
    Analysis.anomaly_detection(spark)

    spark.stop()


if __name__ == "__main__":
    main()
