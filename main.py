from matplotlib import pyplot as plt
from matplotlib.pyplot import figure
from pyspark.sql import SparkSession
from sql.sqls import SqlStrings
import seaborn as sns


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
    total_ratings = spark.sql(SqlStrings.groupby_rating_sql).toPandas()
    # Plotting number of ratings per rating
    total_ratings.plot(x="overall", y="count(1)", kind="bar")
    plt.xlabel('Rating')
    plt.ylabel('Number of Rating')
    plt.title('Number of Rating per Rating')
    plt.show()

    # Calculating number of ratings per rating and year
    total_ratings_year = spark.sql(SqlStrings.groupby_rating_time_sql).toPandas()
    figure(figsize=(20, 6), dpi=80)
    sns.barplot(x="year", y="rank_percentage", hue="overall", data=total_ratings_year)
    plt.ylabel('Number of Rating')
    plt.title('Number of Rating per Year and Rating')
    plt.show()

    totals = spark.sql(SqlStrings.totals).toPandas()
    print(totals)




    spark.stop()


if __name__ == "__main__":
    main()
