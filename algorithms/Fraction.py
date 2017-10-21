# http://interactivepython.org/runestone/static/pythonds/Introduction/ObjectOrientedProgramminginPythonDefiningClasses.html
# Vijayarajan Govindarajan 2017

class Fraction:
    def __init__(self, num, den):
        if den == 0:
            raise ValueError('denominator cannot be zero(0)')
        self.num = num
        self.den = den

    def show(self):
        print(self.num, "/", self.den)


def main():
    fraction = Fraction(3, 7)
    print(fraction.num)
    print(fraction.den)
    print(fraction)


if __name__ == "__main__":
    main()
