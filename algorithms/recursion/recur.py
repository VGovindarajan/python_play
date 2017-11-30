# https://runestone.academy/runestone/static/pythonds/Recursion/pythondsCalculatingtheSumofaListofNumbers.html
# Vijayaarajan Govindarajan

baseStr = "0123456789ABCDEF"
allowedBigchars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
allowedSmallchars = "abcdefghijklmnopqrstuvwxyz"

def sumOfList(listOfNum):
    #print(listOfNum)
    if len(listOfNum) == 1:
        return listOfNum[0]
    else:
        return listOfNum[0] + sumOfList(listOfNum[1:])

def toString(number, base):
    if number < 0:
        return ""
    if number < base:
        return baseStr[number]
    else:
        mod = number%base
        rem = number//base
        return toString(rem, base) + baseStr[mod]

def reverseString(str):
    lenStr = len(str)
    if lenStr <= 1:
        return str
    else:
        return str[lenStr-1:] + reverseString(str[0:lenStr-1])

def getAllowedStr(str):
    retVal = ""
    for s in str:
        if s in allowedSmallchars:
            retVal += s
        elif s in allowedBigchars:
            index = allowedBigchars.index(s)
            retVal += allowedSmallchars[index]
    return retVal

def isPalindrome(str):
    allowedStr = getAllowedStr(str)
    reverseStr = reverseString(allowedStr)
    return allowedStr == reverseStr

def main():
    list_of_ints = [1,2,3,4,5,6,7,8,9,10]
    sum = sumOfList(list_of_ints)
    print(list_of_ints, sum)

    n1= 12345678
    n2= 32432
    print(toString(n1,2))
    print(toString(n1,8))
    print(reverseString(toString(n1,8)))
    print(toString(n1,10))
    print(reverseString(toString(n1,10)))
    print(toString(n1,16))

    strP1 = "rada   r"
    print(strP1, isPalindrome(strP1))

    strP1 = "Reviled did I live, said I, as evil I did deliver"
    print(strP1, isPalindrome(strP1))

    strP1 = "Go hang a salami; I’m a lasagna hog."
    print(strP1, isPalindrome(strP1))

if __name__ == "__main__":
    main()