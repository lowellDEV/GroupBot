def checkString(input,botName):
    print ('input :'+input)
    if botName.lower() in input.lower():
        if '#' in input:
            if '#spam' in input.lower():
                return 1
            elif '#help' in input.lower():
                return 3
            elif '#getmyback' in input.lower():
                return 2
            else:
                return 4
    else:
        return False


    