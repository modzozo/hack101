#Insert dashes '-' between each two neighboring odd numbers in num.

request = raw_input(" Please only enter random numbers:")

def dashInsert(num):
    listNum   = list(num)
    firstNum  = int(listNum[0])
    numArray  = []
    iterateNum  = '' 
    for i in range(len(listNum)-1):
        if(int(listNum[i])%2!=0 and int(listNum[i+1])%2!=0 ):
            numArray.append(-int(listNum[i+1]))
        else:
            numArray.append(int(listNum[i+1]))
    
    numArray.insert(0,(firstNum))
    for i in numArray:
        iterateNum = iterateNum + str(i)
    return (iterateNum)

print  dashInsert(request) 
