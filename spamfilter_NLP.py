def importData(path):
    data = [
        line.rstrip() for line in open(path)
    ]
    print(f'{len(data)} data lines imported!')
    return data

def printData(data):
    for message_index, message in enumerate(data[:10]):
        print(f'{message_index} --> {message}')

def main():
    data = importData('./SMSSpamCollection')
    printData(data)



if __name__ == '__main__':
    main()
    
