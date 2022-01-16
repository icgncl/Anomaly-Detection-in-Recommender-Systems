class FilterData:
    @staticmethod
    def filter_data(initial_data, anomaly_labels):
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
