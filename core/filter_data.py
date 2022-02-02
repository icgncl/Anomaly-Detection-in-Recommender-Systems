import numpy as np

class FilterData:
   @staticmethod
   def filter_data_iqr(initial_data, anomaly_labels):
        IQR_scaler = 1.5
        lower_limit_1 = anomaly_labels.iloc[0, 0] - IQR_scaler * (anomaly_labels.iloc[0, 1] - anomaly_labels.iloc[0, 0])
        upper_limit_1 = anomaly_labels.iloc[0, 1] + IQR_scaler * (anomaly_labels.iloc[0, 1] - anomaly_labels.iloc[0, 0])

        lower_limit_2 = anomaly_labels.iloc[1, 0] - IQR_scaler * (anomaly_labels.iloc[1, 1] - anomaly_labels.iloc[1, 0])
        upper_limit_2 = anomaly_labels.iloc[1, 1] + IQR_scaler * (anomaly_labels.iloc[1, 1] - anomaly_labels.iloc[1, 0])

        lower_limit_3 = anomaly_labels.iloc[2, 0] - IQR_scaler * (anomaly_labels.iloc[2, 1] - anomaly_labels.iloc[2, 0])
        upper_limit_3 = anomaly_labels.iloc[2, 1] + IQR_scaler * (anomaly_labels.iloc[2, 1] - anomaly_labels.iloc[2, 0])

        lower_limit_4 = anomaly_labels.iloc[3, 0] - IQR_scaler * (anomaly_labels.iloc[3, 1] - anomaly_labels.iloc[3, 0])
        upper_limit_4 = anomaly_labels.iloc[3, 1] + IQR_scaler * (anomaly_labels.iloc[3, 1] - anomaly_labels.iloc[3, 0])

        lower_limit_5 = anomaly_labels.iloc[4, 0] - IQR_scaler * (anomaly_labels.iloc[4, 1] - anomaly_labels.iloc[4, 0])
        upper_limit_5 = anomaly_labels.iloc[4, 1] + IQR_scaler * (anomaly_labels.iloc[4, 1] - anomaly_labels.iloc[4, 0])

        filtered_data = initial_data[((initial_data['overall'] == 1)
                                      &
                                      (initial_data['modelRating'] > lower_limit_1)
                                      &
                                      (initial_data['modelRating'] < upper_limit_1))
                                     |
                                     ((initial_data['overall'] == 2)
                                      &
                                      (initial_data['modelRating'] > lower_limit_2)
                                      &
                                      (initial_data['modelRating'] < upper_limit_2))
                                     | ((initial_data['overall'] == 3)
                                        &
                                        (initial_data['modelRating'] > lower_limit_3)
                                        &
                                        (initial_data['modelRating'] < upper_limit_3))
                                     | ((initial_data['overall'] == 4)
                                        &
                                        (initial_data['modelRating'] > lower_limit_4)
                                        &
                                        (initial_data['modelRating'] < upper_limit_4))
                                     | ((initial_data['overall'] == 5)
                                        &
                                        (initial_data['modelRating'] > lower_limit_5)
                                        &
                                        (initial_data['modelRating'] < upper_limit_5))
                                     ]

        return filtered_data
 
   @staticmethod
   def filter_data_std(initial_data):
      initial_pd = initial_data.toPandas()
      std_1 = initial_pd.loc[initial_pd['overall'] == 1]['modelRating'].std()
      std_2 = initial_pd.loc[initial_pd['overall'] == 2]['modelRating'].std()
      std_3 = initial_pd.loc[initial_pd['overall'] == 3]['modelRating'].std()
      std_4 = initial_pd.loc[initial_pd['overall'] == 4]['modelRating'].std()
      std_5 = initial_pd.loc[initial_pd['overall'] == 5]['modelRating'].std()

      filtered_data = initial_data[((initial_data['overall'] == 1)
                                    &
                                    (initial_data['modelRating'] > (1 - 3*std_1))
                                    &
                                    (initial_data['modelRating'] < (1 + 3*std_1)))
                                    |
                                    ((initial_data['overall'] == 2)
                                    &
                                    (initial_data['modelRating'] > (2 - 3*std_2))
                                    &
                                    (initial_data['modelRating'] < (2 + 3*std_2)))
                                    | ((initial_data['overall'] == 3)
                                       &
                                       (initial_data['modelRating'] > (3 - 3*std_3))
                                       &
                                       (initial_data['modelRating'] < (3 + 3*std_3)))
                                    | ((initial_data['overall'] == 4)
                                       &
                                       (initial_data['modelRating'] > (4 - 3*std_4))
                                       &
                                       (initial_data['modelRating'] < (4 + 3*std_4)))
                                    | ((initial_data['overall'] == 5)
                                       &
                                       (initial_data['modelRating'] > (5 - 3*std_5))
                                       &
                                       (initial_data['modelRating'] < (5 + 3*std_5)))
                                    ]

      return filtered_data


   @staticmethod
   def filter_data_percentile(initial_data):
      initial_pd = initial_data.toPandas()
      percentile_1 = np.percentile(initial_pd.loc[initial_pd['overall'] == 1]['modelRating'],[1,99])
      percentile_2 = np.percentile(initial_pd.loc[initial_pd['overall'] == 2]['modelRating'],[1,99])
      percentile_3 = np.percentile(initial_pd.loc[initial_pd['overall'] == 3]['modelRating'],[1,99])
      percentile_4 = np.percentile(initial_pd.loc[initial_pd['overall'] == 4]['modelRating'],[1,99])
      percentile_5 = np.percentile(initial_pd.loc[initial_pd['overall'] == 5]['modelRating'],[1,99])

      filtered_data = initial_data[((initial_data['overall'] == 1)
                                    &
                                    (initial_data['modelRating'] > percentile_1[0])
                                    &
                                    (initial_data['modelRating'] < percentile_1[1]))
                                    | ((initial_data['overall'] == 2)
                                    &
                                    (initial_data['modelRating'] > percentile_2[0])
                                    &
                                    (initial_data['modelRating'] < percentile_2[1]))
                                    | ((initial_data['overall'] == 3)
                                       &
                                       (initial_data['modelRating'] > percentile_3[0])
                                       &
                                       (initial_data['modelRating'] < percentile_3[1]))
                                    | ((initial_data['overall'] == 4)
                                       &
                                       (initial_data['modelRating'] > percentile_4[0])
                                       &
                                       (initial_data['modelRating'] < percentile_4[1]))
                                    | ((initial_data['overall'] == 5)
                                       &
                                       (initial_data['modelRating'] > percentile_5[0])
                                       &
                                       (initial_data['modelRating'] < percentile_5[1]))
                                    ]

      return filtered_data