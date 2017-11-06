#https://runestone.academy/runestone/static/pythonds/BasicDS/ConvertingDecimalNumberstoBinaryNumbers.html
# Vijayarajan Govindarajan 2017

from StackImpl import StackImpl

def baseConverter(integer, base):
    reminderStack = StackImpl()
    digits = "0123456789ABCDEF"

    while integer > 0:
        reminder = integer % base
        reminderStack.push(reminder)
        integer //= base

    returnStr = ""
    while not reminderStack.isEmpty():
        returnStr += digits[reminderStack.pop()]
    return returnStr


def toBinary(base10Integer):
    reminderStack = StackImpl()

    while base10Integer > 0:
        reminder = base10Integer % 2
        reminderStack.push(reminder)
        base10Integer //= 2

    binaryString = ""
    while not reminderStack.isEmpty():
        binaryString += str(reminderStack.pop())

    return binaryString

def main():
    base10Integer = 42
    binaryValue = toBinary(base10Integer)
    binaryValueNew = baseConverter(42,2)
    octaValue = baseConverter(42,8)
    hexaValue = baseConverter(42,16)
    print("Base 10 ", base10Integer, " Binary ", binaryValue)
    print("Base 10 ", base10Integer, " Binary New ", binaryValueNew)
    print("Base 10 ", base10Integer, " Octal ", octaValue)
    print("Base 10 ", base10Integer, " HexaValue ", hexaValue)

if __name__ == "__main__":
    main()