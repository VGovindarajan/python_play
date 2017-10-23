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

    def __str__(self):
        return "%d / %d" % (self.num, self.den)

    def __add__(self, other):
        newnum = (self.num * other.den) + (self.den * other.num)
        newden = self.den * other.den
        common = gcd(newnum, newden)
        return Fraction(newnum / common, newden / common)

    def __sub__(self, other):
        newnum = (self.num * other.den) - (self.den * other.num)
        newden = self.den * other.den
        common = gcd(newnum, newden)
        return Fraction(newnum / common, newden / common)

    def __eq__(self, other):
        left = self.num * other.den
        right = self.den * other.num
        return left == right

def main():
    twofifths = Fraction(2, 5)
    print("twofifths", twofifths)
    onefifths = Fraction(1, 5)
    print("onefifths", onefifths)
    threefifths = twofifths + onefifths
    print(twofifths, "+", onefifths, " = ", threefifths)
    subonefifths = twofifths - onefifths
    print(twofifths, "-", onefifths, " = ", subonefifths)
    sixtenths = Fraction(6, 10)
    print("sixtenths", sixtenths)
    print(threefifths, " & ", sixtenths, "are equal ? ", threefifths == sixtenths)

if __name__ == "__main__":
    main()
