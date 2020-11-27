import csv
import random


def train_test(dataset, test_state):
    test_ratio = 100 * test_state
    train_ratio = 100 - test_ratio
    training_set, testing_set = [], []
    # dataset=[]
    c = 0
    len_train = (len(dataset) * train_ratio) / 100
    len_test = len(dataset) - len_train
    #random.shuffle(data)
    # .....Splitting the dataset.......
    for i in range(int(len_train)):
        training_set.append(dataset[i])
        c += 1
    print(len_train, c)
    for i in range(int(len_train), len(dataset)):
        # if dataset[i] not in training_set:
        testing_set.append(dataset[i])

    return training_set, testing_set


data = []
with open('xssed.csv') as tsv:
    for line in csv.reader(tsv, delimiter=','):
        data.append(list(line))
training_data, testing_data = train_test(data, 0.2)
print(len(training_data), len(testing_data))