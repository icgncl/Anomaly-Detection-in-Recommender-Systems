from pyspark.sql import SparkSession
from core import Analysis, FilterData
from model import Model, RecommendationModel


def main():
    # Initialize Spark
    spark = SparkSession.builder \
        .master("local[2]") \
        .appName("CENG790_Project") \
        .config("spark.executor.memory", "16g") \
        .config("spark.driver.memory", "16g") \
        .getOrCreate() 


    spark.sparkContext.setLogLevel("ERROR")

    # This function creates new csv from dataset
    # In the new csv, ratings were calculated according to their reviewTexts
    Model.create_new_data_w_nlp()

    # Reads the converted csv
    initial_data = spark.read \
        .option("multiline", "true") \
        .option("quote", '"') \
        .option("header", "true") \
        .option("escape", "\\") \
        .option("inferSchema", "true") \
        .option("escape", '"').csv('data/Magazine_Sub_With_Rating.csv').cache()

    anomaly_labels = Analysis.analyzer(spark, initial_data)

    # Finetune the ALS parameters in order to find best model
    finetuning_list, iteration, rank, reg = RecommendationModel.finetuning(initial_data)

    print(finetuning_list)

    print(f"Best model parameters: iteration{iteration}, rank {rank}, regParam {reg}")

    # It filters the anomalies from dataset
    filtered_data_iqr = FilterData.filter_data_iqr(initial_data, anomaly_labels)
    filtered_data_std = FilterData.filter_data_std(initial_data)
    filtered_data_percentile = FilterData.filter_data_percentile(initial_data)
    # In order to feed model with NLP output use label_column as "modelRating"
    # in order to use users' default rating use "overall"
    # label_column = "modelRating"
    # RecommendationModel.rmse_calculate(label_column, initial_data, iteration, rank, reg)
    # RecommendationModel.rmse_calculate(label_column, filtered_data, iteration, rank, reg)
    label_column = "overall"
    RecommendationModel.rmse_calculate(label_column, initial_data, iteration, rank, reg)
    RecommendationModel.rmse_calculate(label_column, filtered_data_iqr, iteration, rank, reg)
    RecommendationModel.rmse_calculate(label_column, filtered_data_std, iteration, rank, reg)
    RecommendationModel.rmse_calculate(label_column, filtered_data_percentile, iteration, rank, reg)

    spark.stop()


if __name__ == "__main__":
    main()
