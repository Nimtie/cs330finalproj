# Unlock Code is 894621
# Lock Code is 894624
import random
import sys


def sec_input(inputType):
    if inputType == "Standard":
        return input("Enter a number: ")
    elif inputType == "Random":
        return str(random.randint(0, 9))


def sec_device(inputType):
    currentState = 'qinit'
    numbersTried = 0
    timesCodeCorrect = 0
    maxRuns = 0
    timesList = []
    if inputType == 'Random':
        while True:
            try:
                maxRuns = int(input('How many times do you want to run this? '))
                if maxRuns <= 0:
                    print('Value not allowed, setting to default of 10')
                    maxRuns = 10
            except ValueError:
                print('Please enter an integer')
            while timesCodeCorrect < maxRuns:
                num = sec_input(inputType)
                test = change_state(currentState, num)
                currentState = test[0]
                numbersTried += 1
                if currentState == 'qunlock' and test[1] == 'unlock':
                    print('unlock')
                    timesList.append(numbersTried)
                    numbersTried = 0
                    timesCodeCorrect += 1
                elif currentState == 'qlock' and test[1] == 'lock':
                    print('lock')
                    timesList.append(numbersTried)
                    numbersTried = 0
                    timesCodeCorrect += 1
            break
        print(timesList)
        print('Min is: ' + str(min(timesList)))
        print('Max is: ' + str(max(timesList)))
        print('Average is: ' + str(sum(timesList) / len(timesList)))

    elif inputType == 'Standard':
        while True:
            num = sec_input(inputType)
            test = change_state(currentState, num)
            currentState = test[0]
            if currentState == 'qunlock' and test[1] == 'unlock':
                print('unlock')
            elif currentState == 'qlock' and test[1] == 'lock':
                print('lock')


def change_state(state, char):
    if not char.isdigit() or len(char) > 1:
        return state, ''

    elif state == 'qinit':
        if char == '8':
            return 'q1', ''
        else:
            return 'qinit', ''
    elif state == 'q1':
        if char == '9':
            return 'q2', ''
        else:
            return 'qinit', ''
    elif state == 'q2':
        if char == '4':
            return 'q3', ''
        else:
            return 'qinit', ''
    elif state == 'q3':
        if char == '6':
            return 'q4', ''
        else:
            return 'qinit', ''
    elif state == 'q4':
        if char == '2':
            return 'q5', ''
        else:
            return 'qinit', ''
    elif state == 'q5':
        if char == '1':
            return 'qunlock', 'unlock'
        elif char == '4':
            return 'qlock', 'lock'
        else:
            return 'qinit', ''
    elif state == 'qunlock':
        if char == '8':
            return 'q1', ''
        else:
            return 'qinit', ''
    elif state == 'qlock':
        if char == '8':
            return 'q1', ''
        else:
            return 'qinit', ''


# Only runs if not in a test environment
if 'unittest' not in sys.modules.keys():
    while True:
        modeInput = input('Choose a mode: \nStandard\nRandom\n')
        if modeInput == 'Standard' or modeInput == 'Random':
            sec_device(modeInput)
            break
        else:
            continue



