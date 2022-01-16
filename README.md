# Anomaly Detection in Recommendation Systems
It is a term project repository for CENG790 course in METU. In this project, product ratings were analyzed according to rating and year.
![total_ratings_per_year](https://github.com/icgncl/CENG790_Project/blob/main/outputs/total_ratings_per_year.png?raw=true)

Also in the project, the product review texts were analyzed semantically with BERT. The output of NLP model is "modelRating" and the dataset was already included product ratings. With these two data, anomalies were detected in the project.

![anomaly_detection](https://github.com/icgncl/CENG790_Project/blob/main/outputs/anomaly_detection.png?raw=true)

Then we have used ALS in order to recommend new magazines. The model was finetuned, best parameters found as iteration: 20, rank: 24, regParam: 0.5 for ALS.
Finally, ALS model was used with original product ratings and ratings generated from product review texts with NLP. 

The RMSE value with original product ratings: 1.649
The RMSE value with ratings generated from product review texts with NLP: 1.504

# Dataset 
In this project, Amazon Review Dataset[1] is used. The dataset was already divided to categories. In this project, "Magazine Subscriptions" category is used;
however, the all categories can be used with this project.

References: 
[1] Justifying recommendations using distantly-labeled reviews and fined-grained aspects. Jianmo Ni, Jiacheng Li, Julian McAuley Empirical Methods in Natural Language Processing (EMNLP), 2019
