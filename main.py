from matplotlib import pyplot as plt
from pyspark.sql import SparkSession
from sql.sqls import SqlStrings

# Initialize Spark
spark = SparkSession.builder \
    .master("local[*]") \
    .appName("CENG790_Project") \
    .getOrCreate()

# read json and convert it to table
magazineDF = spark.read.json('data/Magazine_Subscriptions.json')
magazineDF.createOrReplaceTempView("magazine_table")

# Calculating number of ratings per rating
total_ratings = spark.sql(SqlStrings.groupby_rating_sql).toPandas()

# Plotting number of ratings per rating
total_ratings.plot(x="overall", y="count(1)", kind="bar")
plt.xlabel('Rating')
plt.ylabel('Number of Rating')
plt.title('Number of Rating per Rating')
plt.show()
