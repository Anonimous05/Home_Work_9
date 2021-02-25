class Fraction:

    def __init__(self, numerator, denumerator):
        if denumerator <= 0:
            raise ValueError("Знаменатель не должен = 0!")

        self.numerator = numerator
        self.denumerator = denumerator

    def add(self, numerator2, denumerator2):
        if self.denumerator == denumerator2:
            numerator = self.numerator + numerator2
            denumerator = self.denumerator
            print(f"{numerator}/{denumerator}")
            return Fraction(numerator, denumerator)
        else:
            numerator = self.numerator * denumerator2 + numerator2 * self.denumerator
            denumerator = self.denumerator * denumerator2
            print(f"{numerator}/{denumerator}")
            return Fraction(numerator, denumerator)

    def sub(self, numerator2, denumerator2):
        if self.denumerator == denumerator2:
            numerator = self.numerator - numerator2
            denumerator = self.denumerator
            print(f"{numerator}/{denumerator}")
            return Fraction(numerator, denumerator)
        else:
            numerator = self.numerator * denumerator2 - numerator2 * self.denumerator
            denumerator = self.denumerator * denumerator2
            print(f"{numerator}/{denumerator}")
            return Fraction(numerator, denumerator)

    def mult(self, numerator2, denumerator2):
        numerator = self.numerator * numerator2
        denumerator = self.denumerator * denumerator2
        print(f"{numerator}/{denumerator}")
        return Fraction(numerator, denumerator)

    def divi(self, numerator2, denumerator2):
        numerator = self.numerator * denumerator2
        denumerator = self.denumerator * numerator2
        print(f"{numerator}/{denumerator}")
        return Fraction(numerator, denumerator)


drob1 = Fraction(3, 7)
drob1.mult(4, 5)