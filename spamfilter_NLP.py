import pandas as pd


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


def main():
    path = './SMSSpamCollection'
    # data = importData(path)
    # printData(data)
    df = convertDataToDataFrame(path)


if __name__ == '__main__':
    main()
