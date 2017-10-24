# http://interactivepython.org/runestone/static/pythonds/Introduction/ObjectOrientedProgramminginPythonDefiningClasses.html
# Vijayarajan Govindarajan 2017


def gcd(num, den):
    while num % den != 0:
        oldnum = num
        oldden = den

        num = oldden
        den = oldnum % oldden
    return den

class Fraction:
    def __init__(self, num, den):
        if den == 0:
            raise ValueError('denominator cannot be zero(0)')
        self.num = num
        self.den = den

    def __repr__(self):
        return "%d / %d" % (self.num, self.den)

    def __str__(self):
        return "%d / %d" % (self.num, self.den)

    def __add__(self, other):
        newnum = (self.num * other.den) + (self.den * other.num)
        newden = self.den * other.den
        common = gcd(newnum, newden)
        return Fraction(newnum / common, newden / common)

    def __sub__(self, other):
        newnum = (self.num * other.num) - (self.den * other.num)
        newden = self.den * other.den
        common = gcd(newnum, newden)
        return Fraction(newnum / common, newden / common)

    def __mul__(self, other):
        newnum = self.num * other.num
        newden = self.den * other.den
        common = gcd(newnum, newden)
        return Fraction(newnum / common, newden / common)

    def __truediv__(self, other):
        newnum = self.num * other.den
        newden = self.den * other.num
        common = gcd(newnum, newden)
        return Fraction(newnum / common, newden / common)

    def __eq__(self, other):
        left = self.num * other.den
        right = self.den * other.num
        return left == right

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        left = self.num * other.den
        right = self.den * other.num
        return left < right

    def __le__(self, other):
        left = self.num * other.den
        right = self.den * other.num
        return left <= right

    def __gt__(self, other):
        left = self.num * other.den
        right = self.den * other.num
        return left > right

    def __ge__(self, other):
        left = self.num * other.den
        right = self.den * other.num
        return left >= right

def main():
    twofifths = Fraction(2, 5)
    print("twofifths", twofifths)
    onefifths = Fraction(1, 5)
    print("onefifths", onefifths)
    sixtenths = Fraction(6, 10)
    print("sixtenths", sixtenths)
    threefifths = twofifths + onefifths
    print(twofifths, "+", onefifths, " = ", threefifths)
    subonefifths = twofifths - onefifths
    print(twofifths, "-", onefifths, " = ", subonefifths)

    print("****** operator overloading ******")
    ## == operator
    print(threefifths, " == ", sixtenths, " = ", threefifths == sixtenths)
    ## != operator
    print(threefifths, " != ", sixtenths, " = ", threefifths != sixtenths)
    ## * operator
    print(threefifths, " * ", sixtenths, " = ", threefifths * sixtenths)
    ## * operator
    print(threefifths, " / ", sixtenths, " = ", threefifths / sixtenths)

    ## > operator
    print(threefifths, " > ", onefifths, " = ", threefifths > onefifths)
    ## >= operator
    print(threefifths, " >= ", sixtenths, " = ", threefifths >= sixtenths)

    ## < operator
    print(threefifths, " < ", twofifths, " = ", threefifths < twofifths)
    ## <= operator
    print(onefifths, " <= ", twofifths, " = ", onefifths <= twofifths)

if __name__ == "__main__":
    main()
