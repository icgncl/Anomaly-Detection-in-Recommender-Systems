import matplotlib.pyplot as plt
import pandas as pd
from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.ml.feature import StringIndexer
from pyspark.ml.recommendation import ALS


class RecommendationModel:

    @staticmethod
    def finetuning(data):
        data = StringIndexer(inputCol="reviewerID", outputCol="reviewerID2").fit(data).transform(data)
        data = StringIndexer(inputCol="asin", outputCol="asin2").fit(data).transform(data)

        (training, test) = data.randomSplit([0.8, 0.2], seed=10)

        iteration = [12, 16, 20]
        rank = [16, 20, 24]
        regParam = [0.1, 1, 0.5]
        initial_RMSE = 100
        final_iteration = 12
        final_rank = 16
        final_reg = 0.1
        finetuning_list = []
        i = 0
        for each_iteration in iteration:
            for each_rank in rank:
                for each_reg in regParam:
                    als = ALS(maxIter=each_iteration, regParam=each_reg, userCol="reviewerID2", itemCol="asin2",
                              ratingCol="overall",
                              coldStartStrategy="drop", seed=10, rank=each_rank)
                    model = als.fit(training)

                    # Evaluate the model by computing the RMSE on the test data
                    predictions = model.transform(test)
                    evaluator = RegressionEvaluator(metricName="rmse", labelCol="overall",
                                                    predictionCol="prediction")
                    rmse = evaluator.evaluate(predictions)

                    finetuning_list.append(
                        {'iteration': each_iteration, 'rank': each_rank, 'reg': each_reg, 'rmse': rmse})
                    i += 1
                    if rmse < initial_RMSE:
                        initial_RMSE = rmse
                        final_iteration = each_iteration
                        final_rank = each_rank
                        final_reg = each_reg
        finetuning_df = pd.DataFrame(finetuning_list)

        def label_race(row):
            return f"rank{row['rank']} iteration{row['iteration']} reg {row['reg']}"

        finetuning_df['all'] = finetuning_df.apply(lambda row: label_race(row), axis=1)

        plt.figure(4)
        pd.plotting.parallel_coordinates(
            finetuning_df, 'all'
        )
        plt.title('HyperParameter Tuning')
        plt.savefig('outputs/parameters.png')
        return finetuning_list, final_iteration, final_rank, final_reg

    @staticmethod
    def rmse_calculate(label_column, data, iteration, rank, reg):

        data = StringIndexer(inputCol="reviewerID", outputCol="reviewerID2").fit(data).transform(data)
        data = StringIndexer(inputCol="asin", outputCol="asin2").fit(data).transform(data)

        (training, test) = data.randomSplit([0.8, 0.2], seed=11)

        als = ALS(maxIter=iteration, regParam=reg, userCol="reviewerID2", itemCol="asin2",
                  ratingCol=label_column,
                  coldStartStrategy="drop", seed=11, rank=rank)
        model = als.fit(training)

        # Evaluate the model by computing the RMSE on the test data
        predictions = model.transform(test)
        evaluator = RegressionEvaluator(metricName="rmse", labelCol=label_column,
                                        predictionCol="prediction")
        rmse = evaluator.evaluate(predictions)
        print(f"Root-mean-square error for {label_column}: RMSE=" + str(rmse))
