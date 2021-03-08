import pandas as pd
import string
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report


def importData(path):
    data = [
        line.rstrip() for line in open(path)
    ]
    print(f'{len(data)} data lines imported!')
    return data




def main():
    path = './SMSSpamCollection'
    # data = importData(path)
    # printData(data)
    df = convertDataToDataFrame(path)
    transformer = countVectorizerModelCreation()
    # transformer = tfidfVectorizerModelCreation()
    X = fitVectorizerModel(transformer,df)
    transformedData = transformVectorizerModel(X,df)

    tf_idftransformer = tfidfTransformerModelCreation()
    X = fitTransformerModel(tf_idftransformer, transformedData)
    tf_idftransformedData = transformTransformerModel(X, transformedData)

    spam_detect_model = trainModel(tf_idftransformedData,df)
    y_pred = testModel(spam_detect_model, tf_idftransformedData)

    print(classification_report(df['label'],y_pred))










    


if __name__ == '__main__':
    main()
