#Bryan Fisk
#2/17/19

epoch_number = 10
training_rate = 1

def remove_5000(lst):
    while 5000 in lst:
        lst.remove(5000)
    return lst

def infile(s):
    with open(s) as file:
        input = list(file.read().split())
        file.close()
        return input

def formatinput(lst):
    input = [list(map(int, i.split(','))) for i in lst]
    y = []
    X = []
    for i in input:
        i.insert(5000, 1)
        i = remove_5000(i)
        y.append(i[0])
        X.append(i[1:])
    X = [list(set(i)) for i in X]
    return X, y
    
def maininput(s):
    input = infile(s)
    X, y = formatinput(input)
    return X, y

train_X, train_y = maininput('train.txt')
test_X, test_y = maininput('test.txt')

weights = [0 for k in range(5001)]

for epoch in range(epoch_number):
    activation = 0
    for index, X in enumerate(train_X):
        activation = 0
        f_X = 0
        for word in X:
            activation += weights[word]
        if activation > 0:
            f_X = 1
        if f_X != train_y[index]:
            for word in X:
                weights[word] = weights[word] + training_rate * (train_y[index] - f_X)

test = []
for index, X in enumerate(test_X):
    activation = 0
    f_X = 0
    for word in X:
        activation += weights[word]
    if activation > 0:
        f_X = 1
    test.append(f_X)

count = 0
for c in range(len(test)):
    if test[c] == test_y[c]:
        count += 1

print(count / len(test_y) * 100)
