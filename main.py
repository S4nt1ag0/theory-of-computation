'''
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
'''
states = ['0', '1', '2', '3', '4']
alphabet = ['a', 'b']
ribbonAlphabet = ['A', 'B', '*']
leftSymbol = '<'
whiteSymbol = '*'
futureStatesDictionary = {'0': {}, '1': {}, '2': {}, '3': {}, '4': {}, ('0', 'a'): [['1', 'A', 'D']], ('1', 'a'): [['1', 'a', 'D']], ('1', 'B'): [['1', 'B', 'D']], ('1', 'b'): [['2', 'B', 'E']], ('2', 'B'): [['2', 'B', 'E']], ('2', 'a'): [['2', 'a', 'E']], ('2', 'A'): [['0', 'A', 'D']], ('0', 'B'): [['3', 'B', 'D']], ('3', 'B'): [['3', 'B', 'D']], ('3', '*'): [['4', '*', 'E']]}
'''
initialState = input()
finalStates = input().split(' ')

words = input().split(' ')
'''
initialState = '0'
finalStates = ['4']

words = ['*', 'ab', 'ba', 'abb', 'aab', 'aabb']

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
