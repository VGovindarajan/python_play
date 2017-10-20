#http://interactivepython.org/runestone/static/pythonds/Introduction/DefiningFunctions.html
#Vijayarajan Govindarajan 2017
import random

monkey_string = 'methinks it is like a weasel'
alphabets = 'abcdefghijklmnopqrstuvwxyz '

def get_random_char():
    randomNum = random.randint(0, (len(alphabets)-1))
    #print('gereandomchar', randomNum)
    return alphabets[randomNum]

def get_random_monkey_string(count):
    retval = ''
    for i in range(0,count):
        ch = get_random_char()
        retval = retval+ch
    if len(retval) != count :
        raise ValueError("len is not equal")
    return retval

def get_hill_climbing_monkey_string(stringtochange, chposition):
    ch = get_random_char()
    stringtoreturn = stringtochange[0:chposition] + ch + stringtochange[chposition+1:]
    return stringtoreturn

def check_monkey_book_typing_count():
    count = 0
    maxscore = 0
    max_score_string = ''
    while(True):
        count += 1
        checkstring = get_random_monkey_string(len(monkey_string))
        #print(count, checkstring)
        score = score_monkey_string(checkstring)
        if score > maxscore:
            maxscore = score
            max_score_string = checkstring
        if checkstring == monkey_string :
            break
        if count%10000 == 0:
            print(count, maxscore, max_score_string)
    return count


def check_hill_climbing_monkey_book_typing_count():
    count = 0
    passedStr = get_random_monkey_string(len(monkey_string))
    while(True):
        for j in range(0, len(monkey_string)):
            runInner = True
            while(runInner):
                count += 1
                checkstring = get_hill_climbing_monkey_string(passedStr, j)
                isequal = is_monkey_string_equal_atposition(checkstring, j)
                #print(j, monkey_string[j], checkstring[j])
                if isequal:
                    passedStr = checkstring
                    print(passedStr)
                    runInner = False
        print(count, passedStr)
        if passedStr == monkey_string :
            break
        return count

def score_monkey_string(stringtocheck):
    score = 0
    for i in range(0,len(stringtocheck)):
        if monkey_string[i]==stringtocheck[i]:
            score+=1
    return score

def is_monkey_string_equal_atposition(stringtocheck, chposition):
    return monkey_string[chposition]==stringtocheck[chposition]

def main():
    print("In main")
    count = check_hill_climbing_monkey_book_typing_count()
    print(count)

if __name__ == "__main__":
    main()