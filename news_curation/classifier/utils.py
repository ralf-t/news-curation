import joblib
import pandas as pd
from sklearn import feature_extraction
from os.path import join

def predict(text):
    '''
        Passes text input to the fake news classifier and returns prediction.

        params:
            text : string 

        return:
            0 : real news
            1 : fake news

    '''

    # load model
    # model = joblib.load('./classifier/poormans-model.pkl')
    model = joblib.load(join('news_curation','classifier','poormans-model.pkl'))
    
    # dataset corpus
    corpus = pd.read_csv(join('news_curation','classifier','data.csv'))
    
    # vectorizer
    count_vectorizer = feature_extraction.text.CountVectorizer()
    
    # fit vectorizer to corpus
    count_vectorizer.fit_transform(corpus["article"])

    # vectorized representation of the text
    text = count_vectorizer.transform([text]).toarray()

    prediction = model.predict(text)[0]

    return prediction