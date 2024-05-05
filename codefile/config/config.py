import pickle

class Config:
    model = pickle.load(open("model/model.pkl", 'rb'))
    cv = pickle.load(open("model/vectorizer.pkl", 'rb'))