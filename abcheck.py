#The function should return true if the characters a and b are separated by exactly 3 places anywhere in the string at least once.

request=raw_input("Please enter only random strings:")

def ABCheck(str):
    strList = list(str)
    aList = [i for i, x in enumerate(strList) if x == "a"]
    bList = [i for i, x in enumerate(strList) if x == "b"]
    if len(aList) == 0 or len(bList) == 0:
        return False

    for i in range(0, len(aList)):
        for j in range(0, len(bList)):
            if abs(aList[i]-bList[j]) < 3:
                return False
    return True

print ABCheck(request) 
