#https://runestone.academy/runestone/static/pythonds/BasicDS/ConvertingDecimalNumberstoBinaryNumbers.html
#https://runestone.academy/runestone/static/pythonds/BasicDS/InfixPrefixandPostfixExpressions.html?lastPosition=2624
# Vijayarajan Govindarajan 2017

from StackImpl import StackImpl

postFixPrec = {}
postFixPrec["*"] = 3
postFixPrec["/"] = 3
postFixPrec["+"] = 2
postFixPrec["-"] = 2
postFixPrec["("] = 1

alphabets = ("A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z")
numbers = ("0","1","2","3","4","5","6","7","8","9")
operators = ("*","/","+","-")

def infixToPostfix(infixExpression):
    operatorStack = StackImpl()
    postFixList = []

    tokenList = infixExpression.split()
    for token in tokenList:
        if token in alphabets or token in numbers:
            postFixList.append(token)
        elif token == '(':
            #opening bracket
            operatorStack.push(token)
        elif token == ')':
            #closing bracket
            topToken = operatorStack.pop()
            while topToken != '(':
                postFixList.append(topToken)
                topToken = operatorStack.pop()
        else:
            while (not operatorStack.isEmpty() and \
                    postFixPrec[operatorStack.peek()] >= postFixPrec[token]):
                    postFixList.append(operatorStack.pop())
            operatorStack.push(token)

    while not operatorStack.isEmpty():
        postFixList.append(operatorStack.pop())

    return " ".join(postFixList)


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


def doTheMath(operator, operand1, operand2):
    if operator == "*":
        return operand1*operand2
    elif operator == "/":
        return operand1/operand2
    elif operator == "+":
        return operand1+operand2
    else:
        return operand1-operand2


def postFixEvaluation(postFixExpression):
    operandStack = StackImpl()
    tokenList = postFixExpression.split()

    for token in tokenList:
        if token in numbers:
            operandStack.push(int(token))
        else:
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            result = doTheMath(token, operand1, operand2)
            operandStack.push(result)

    return operandStack.pop()

def main():
    base10Integer = 256
    binaryValue = toBinary(base10Integer)
    binaryValueNew = baseConverter(base10Integer,2)
    octaValue = baseConverter(base10Integer,8)
    hexaValue = baseConverter(base10Integer,16)
    print("Base 10 ", base10Integer, " Binary ", binaryValue)
    print("Base 10 ", base10Integer, " Binary New ", binaryValueNew)
    print("Base 10 ", base10Integer, " Octal ", octaValue)
    print("Base 10 ", base10Integer, " HexaValue ", hexaValue)

    infix = "( A * B ) * ( C * D ) + D * E "
    infix2 = "( A + B ) * C - ( D - E ) * ( F + G )"
    postFix = infixToPostfix(infix)
    print(infix," in postfix is = ", postFix)
    print(infix2," in postfix is = ", infixToPostfix(infix2))

    infix3 = "( 7 + 8 ) / ( 3 + 2 )"
    postfix3 = infixToPostfix(infix3)
    postfixEval3 = postFixEvaluation(postfix3)
    print(infix3," in postfix is = ", postfix3 , " eval is  ", postfixEval3 )

    infix3 = "( 7 * 8 ) - ( 2 * 2 ) * 6 + 3 * 2"
    postfix3 = infixToPostfix(infix3)
    postfixEval3 = postFixEvaluation(postfix3)
    print(infix3," in postfix is = ", postfix3 , " eval is  ", postfixEval3 )

if __name__ == "__main__":
    main()