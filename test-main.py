from datetime import datetime
states = ['0','1','2','3','4']
alphabet = ['a','b']
ribbonAlphabet = ['A','B','*']
leftSymbol = '<'
whiteSymbol = '*'
transactions = 10
quintuplas = ["0 a 1 A D", "1 a 1 a D", "1 B 1 B D", "1 b 2 B E", "2 B 2 B E", "2 a 2 a E", "2 A 0 A D", "0 B 3 B D", "3 B 3 B D", "3 * 4 * E"]

futureStatesDictionary = {}

for i in range(transactions):
    stateFrom, letterRead, stateTo, letterWrite, direction = quintuplas[i].split()
    if (stateFrom, letterRead) not in futureStatesDictionary:
        futureStatesDictionary[(stateFrom, letterRead)] = []

    futureStatesDictionary[(stateFrom, letterRead)].append([stateTo, letterWrite, direction])

initialState = '0'
finalStates = ['4']

wa = 'a'
wb = 'b'

words = []

for i in range(30):
   w = wa+wb
   words.append(w)
   wa = wa+'a'
   wb = wb+'b'

wordAnalytics = {}
for i in range(100):
    for word in words:
        data1 = datetime.now()
        time1 = datetime.timestamp(data1)
        ribbon = list((leftSymbol + word + whiteSymbol))
        path = [(initialState, 1, ribbon)]

        while True:
            state, position, ribbonElements = path.pop()

            if (state, ribbonElements[position]) in futureStatesDictionary:
                for transaction in futureStatesDictionary[(state, ribbonElements[position])]:
                    elementsOfRibbon = []

                    for element in ribbonElements:
                        elementsOfRibbon.append(element)

                    if ribbonElements[position] == whiteSymbol:
                        ribbonElements.append(whiteSymbol)
                        elementsOfRibbon.append(whiteSymbol)

                    elementsOfRibbon[position] = transaction[1]

                    if transaction[2] == 'E':
                        path.append((transaction[0], (position - 1), elementsOfRibbon))
                    elif transaction[2] == 'D':
                        path.append((transaction[0], (position + 1), elementsOfRibbon))
                    elif transaction[2] == 'I':
                        path.append((transaction[0], position, elementsOfRibbon))

            else:
                if state in finalStates:
                    break
                if len(path) == 0:
                    break

        data2 = datetime.now()
        time2 = datetime.timestamp(data2)
        if not wordAnalytics.get(word):
            wordAnalytics[word] = 0.0

        wordAnalytics[word] += (time2 - time1)

for word in wordAnalytics.keys():
    wordAnalytics[word] = wordAnalytics[word] / 1000;
    print(len(word))