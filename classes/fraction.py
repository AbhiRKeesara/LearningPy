# standard operators -> https://docs.python.org/3/library/operator.html


def gcd(num1, num2):
    while num1 % num2 != 0:
        num1, num2 = num2, num1 % num2
    return num2


class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def __str__(self):
        return f"{self.num}/{self.den}"

    def __add__(self, other_fraction):
        new_num = self.num * other_fraction.den + self.den * other_fraction.num
        new_den = self.den * other_fraction.den
        common = gcd(new_num, new_den)
        return Fraction(new_num // common, new_den // common)

    def __sub__(self, other_fraction):
        new_num = self.num * other_fraction.den - self.den * other_fraction.num
        new_den = self.den * other_fraction.den
        common = gcd(new_num, new_den)
        return Fraction(new_num // common, new_den // common)

    def __eq__(self, other_fraction):
        first_num = self.num * other_fraction.den
        second_num = self.den * other_fraction.num

        return first_num == second_num

    def __lt__(self, other_fraction):
        first_num = self.num * other_fraction.den
        second_num = self.den * other_fraction.num

        return first_num < second_num

    def __gt__(self, other_fraction):
        first_num = self.num * other_fraction.den
        second_num = self.den * other_fraction.num

        return first_num > second_num

    def __mul__(self, other_fraction):
        new_num = self.num * other_fraction.num
        new_den = self.den * other_fraction.den
        common = gcd(new_num, new_den)
        return Fraction(new_num // common, new_den // common)

    def __truediv__(self, other_fraction):
        new_num = self.num * other_fraction.den
        new_den = self.den * other_fraction.num
        common = gcd(new_num, new_den)

        return Fraction(new_num // common, new_den // common)


f1 = Fraction(1, 4)
f2 = Fraction(1, 2)

f3 = f1 + f2

print(f3)

print(f1 == f2)

print(f1 * f2)

print(f1 / f2)

print(f1 < f2)
print(f1 > f2)
