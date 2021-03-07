import pandas as pd
import string
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer 


def importData(path):
    data = [
        line.rstrip() for line in open(path)
    ]
    print(f'{len(data)} data lines imported!')
    return data


def printData(data):
    for message_index, message in enumerate(data[:10]):
        print(f'{message_index} --> {message}')


def convertDataToDataFrame(path):
    df = pd.read_csv(path, sep='\t', names=['label', 'msg'] )
    return df

def dataPreprocessing(df):
    nopunc = [char for char in df if char not in string.punctuation]
    nopunc = ''.join(nopunc)
    return [word for word in nopunc.split() if word.lower() not in stopwords.words('english'))]

def countVectorizerModelCreation():
    transformer = CountVectorizer(analyzer=dataPreprocessing)
    return transformer


def fitModel(transformer,df):
    X = transformer.fit(df['msg'])
    return X


def main():
    path = './SMSSpamCollection'
    # data = importData(path)
    # printData(data)
    df = convertDataToDataFrame(path)
    transformer = CountVectorizer()
    X = fitModel(transformer,df)



    


if __name__ == '__main__':
    main()
