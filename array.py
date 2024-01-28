testArray = []
testDict = {}

def addToList(list, number):
    list.append(number)

for i in range(100):
    x = i % 13
    addToList(testArray, x)

for i in testArray:
    value = testDict.get(i)
    if value == None:
        testDict[i] = 1
    else:
        testDict[i] += 1
def getFactor(num):
    if num == 1:
        return 1
    return num * getFactor(num - 1)

for value in testDict.values():
    print(getFactor(value))


