import json
from csv import DictWriter

import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification


class Model:
    @staticmethod
    def model_insertion():
        tokenizer = AutoTokenizer.from_pretrained("nlptown/bert-base-multilingual-uncased-sentiment")
        model = AutoModelForSequenceClassification.from_pretrained("nlptown/bert-base-multilingual-uncased-sentiment")

        return tokenizer, model

    @staticmethod
    def prediction(tokenizer, model, sentence):
        inputs = tokenizer(sentence, return_tensors="pt")
        outputs = model(**inputs)
        softmax = torch.nn.Softmax(dim=1)
        return softmax(outputs.logits)[0]

    @staticmethod
    def create_new_data_w_nlp():
        tokenizer, model = Model.model_insertion()
        data = [json.loads(line) for line in open('data/Magazine_Subscriptions.json', 'r')]
        ind = 0
        with open("data/Magazine_Sub_With_Rating.csv", 'a', newline='') as file:
            for each_review in data:
                try:
                    if ind == 0:
                        kys = list(each_review.keys())
                        kys.append("modelRating")
                        kys.append("modelRatingDiscrete")
                        kys.append("style")
                        dictwriter_obj = DictWriter(file, fieldnames=kys)
                        dictwriter_obj.writeheader()
                    text = each_review['reviewText']
                    text = text.replace('\n', ' ')
                    probstorch = Model.prediction(tokenizer, model, text)
                    score = 0
                    for i in range(1, 6):
                        score += probstorch[i - 1].item() * i
                    each_review['modelRating'] = score
                    each_review['modelRatingDiscrete'] = torch.argmax(probstorch).item() + 1
                    ind += 1
                    dictwriter_obj.writerow(each_review)
                except Exception as e:
                    print(e)
                    pass
        file.close()
