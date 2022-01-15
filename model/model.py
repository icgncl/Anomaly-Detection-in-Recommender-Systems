import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification


class Model:
    @staticmethod
    def model_insertion():
        tokenizer = AutoTokenizer.from_pretrained("nlptown/bert-base-multilingual-uncased-sentiment")
        model = AutoModelForSequenceClassification.from_pretrained("nlptown/bert-base-multilingual-uncased-sentiment")

        return tokenizer, model

    @staticmethod
    def prediction(sentence):
        tokenizer, model = Model.model_insertion()
        inputs = tokenizer(sentence, return_tensors="pt")
        outputs = model(**inputs)
        softmax = torch.nn.Softmax(dim=1)
        return (softmax(outputs.logits))