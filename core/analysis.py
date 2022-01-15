from sql import SqlStrings
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import seaborn as sns


class Analysis:
    @staticmethod
    def number_of_ratings_per_rating(spark):
        total_ratings = spark.sql(SqlStrings.groupby_rating_sql).toPandas()
        # Plotting number of ratings per rating
        total_ratings.plot(x="overall", y="count(1)", kind="bar")
        plt.xlabel('Rating')
        plt.ylabel('Number of Rating')
        plt.title('Number of Rating per Rating')
        plt.savefig('outputs/total_ratings.png')

    @staticmethod
    def number_of_ratings_per_rating_n_year(spark):
        total_ratings_year = spark.sql(SqlStrings.groupby_rating_time_sql).toPandas()
        figure(figsize=(20, 6), dpi=80)
        sns.barplot(x="year", y="rank_percentage", hue="overall", data=total_ratings_year)
        plt.ylabel('Number of Rating')
        plt.title('Number of Rating per Year and Rating')
        plt.savefig('outputs/total_ratings_per_year.png')

    @staticmethod
    def calculate_totals(spark):
        totals = spark.sql(SqlStrings.totals).toPandas()
        print(totals)

    @staticmethod
    def anomaly_detection(spark):
        new_data = spark.read\
            .option("multiline", "true")\
            .option("quote", '"')\
            .option("header", "true")\
            .option("escape", "\\")\
            .option("inferSchema", "true")\
            .option("escape", '"').csv('data/Magazine_Sub_With_Rating.csv')

        sns.boxplot(x="overall", y="modelRating", data=new_data.toPandas())
        plt.xlabel('Overall Rating')
        plt.ylabel("NLP Model Rating")
        plt.title('Anomaly Detection')
        plt.savefig('outputs/anomaly_detection.png')
        plt.show()
