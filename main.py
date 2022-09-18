states = input().split()
alphabet = input().split()
ribbonAlphabet = input().split()
leftSymbol = input()
whiteSymbol = input()
transactions = int(input())

futureStatesDictionary = {}

for i in range(transactions):
    stateFrom, letterRead, stateTo, letterWrite, direction = input().split()
    if (stateFrom, letterRead) not in futureStatesDictionary:
        futureStatesDictionary[(stateFrom, letterRead)] = []

    futureStatesDictionary[(stateFrom, letterRead)].append([stateTo, letterWrite, direction])

initialState = input()
finalStates = input().split()

words = input().split()

for word in words:
    ribbon = list((leftSymbol + word + whiteSymbol))
    stack = [(initialState, 1, ribbon)]

    while True:
        state, position, ribbonElements = stack.pop()

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
                    stack.append((transaction[0], (position - 1), elementsOfRibbon))
                elif transaction[2] == 'D':
                    stack.append((transaction[0], (position + 1), elementsOfRibbon))
                elif transaction[2] == 'I':
                    stack.append((transaction[0], position, elementsOfRibbon))
        else:
            if state in finalStates:
                print('S')
                break
            if len(stack) == 0:
                print('N')
                break