class Fraction():

    def init(self, num, den):  # num числитель, den знаменатель
        if den == 0:
            raise ValueError("Знаменатель не может быть нулем")

        self.num = num
        self.den = den

    def str(self):
        return str(self.num) + '/' + str(self.den)


    def add(self,fraction2):
        a1 = self.num * fraction2.den + self.den * fraction2.den
        b1 = fraction2.den * self.den
        return Fraction(a1, b1)

    def sub(self,fraction2):
        a2 = self.num * fraction2.den - self.den * fraction2.den
        b2 = fraction2.den * self.den
        return Fraction(a2, b2)

    def mul(self,fraction2):
        a = self.num*fraction2.num
        b = self.den*fraction2.den

        return Fraction(a,b)

    def truediv(self,fraction2):
        a3 = self * self.invert(fraction2)
        return Fraction(a3)

    def repr(self):
        return '{}/{}'.format(self.num, self.den)
