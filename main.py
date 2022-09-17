states = input().split(' ')
alphabet = input().split(' ')
ribbonAlphabet = input().split(' ')
leftSymbol = input()
whiteSymbol = input()
transactions = int(input())



futureStatesDictionary = {}

for state in states:
    futureStatesDictionary[state] = {}

for i in range(transactions):
    stateFrom, letterRead, stateTo, letterWrite, direction = input().split(' ')

    if (stateFrom, letterRead) not in futureStatesDictionary[stateFrom]:
        futureStatesDictionary[(stateFrom, letterRead)] = []

    futureStatesDictionary[(stateFrom, letterRead)].append([stateTo, letterWrite, direction])

initialState = input()
finalStates = input().split(' ')

words = input().split(' ')

for word in words:
    ribbon = list((leftSymbol+word+whiteSymbol))
    path = [(initialState, 1, ribbon)]
    flag = 0

    while True:
        state, position, ribbonElements = path.pop();

        if (state, ribbonElements[position]) in futureStatesDictionary:
            for transaction in futureStatesDictionary[(state, ribbonElements[position])]:
                elementsOfRibbon = []
                for element in ribbonElements:
                    elementsOfRibbon.append(element)

                if elementsOfRibbon[position] == whiteSymbol:
                    elementsOfRibbon.append(whiteSymbol)
                    ribbonElements.append(whiteSymbol)

                elementsOfRibbon[position] = transaction[1]

                if transaction[2] == 'E':
                    path.append((transaction[0],position - 1, elementsOfRibbon))
                elif transaction[2] == 'D':
                    path.append((transaction[0], position + 1, elementsOfRibbon))
                elif transaction[2] == 'I':
                    path.append((transaction[0], position, elementsOfRibbon))
        else:
            if state in finalStates:
                print('S')
                break
            if len(path) == 0:
                print('N')
                break