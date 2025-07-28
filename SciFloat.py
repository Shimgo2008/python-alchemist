class SciFloat:
    def __init__(self, mantissa: float, exponent: int):
        self.mantissa = mantissa
        self.exponent = exponent
        self._normalize()

    def _normalize(self):
        while abs(self.mantissa) >= 10:
            self.mantissa /= 10
            self.exponent += 1
        while abs(self.mantissa) < 1 and abs(self.mantissa) != 0:
            self.mantissa *= 10
            self.exponent -= 1

    def __add__(self, other):
        if isinstance(other, SciFloat):
            if self.exponent == other.exponent:
                return SciFloat(self.mantissa + other.mantissa, self.exponent)
            else:
                exponent = max(self.exponent, other.exponent)
                mantissa = self.mantissa * (10 ** (exponent - self.exponent)) + other.mantissa * (10 ** (exponent - other.exponent))
                return SciFloat(mantissa, exponent)
        elif isinstance(other, (float, int)):
            return self + SciFloat(other, 0)
        else:
            raise TypeError("Unsupported operand type for +")

    def __sub__(self, other):
        if isinstance(other, SciFloat):
            if self.exponent == other.exponent:
                return SciFloat(self.mantissa - other.mantissa, self.exponent)
            else:
                exponent = max(self.exponent, other.exponent)
                mantissa = self.mantissa * (10 ** (exponent - self.exponent)) - other.mantissa * (10 ** (exponent - other.exponent))
                return SciFloat(mantissa, exponent)
        elif isinstance(other, (float, int)):
            return self - SciFloat(other, 0)
        else:
            raise TypeError("Unsupported operand type for -")

    def __mul__(self, other):
        if isinstance(other, SciFloat):
            return SciFloat(self.mantissa * other.mantissa, self.exponent + other.exponent)
        elif isinstance(other, (float, int)):
            return self * SciFloat(other, 0)
        else:
            raise TypeError("Unsupported operand type for *")

    def __truediv__(self, other):
        if isinstance(other, SciFloat):
            return SciFloat(self.mantissa / other.mantissa, self.exponent - other.exponent)
        elif isinstance(other, (float, int)):
            return self / SciFloat(other, 0)
        else:
            raise TypeError("Unsupported operand type for /")

    def __eq__(self, other):
        if isinstance(other, SciFloat):
            return self.mantissa == other.mantissa and self.exponent == other.exponent
        elif isinstance(other, (float, int)):
            return self == SciFloat(other, 0)
        else:
            return NotImplemented

    def __lt__(self, other):
        if isinstance(other, SciFloat):
            if self.exponent == other.exponent:
                return self.mantissa < other.mantissa
            else:
                return self.exponent < other.exponent
        elif isinstance(other, (float, int)):
            return self < SciFloat(other, 0)
        else:
            return NotImplemented

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __gt__(self, other):
        return not self.__lt__(other) and not self.__eq__(other)

    def __ge__(self, other):
        return not self.__lt__(other)

    def __str__(self):
        return f"{self.mantissa}e{self.exponent}"

    def __repr__(self):
        return f"SciFloat({self.mantissa}, {self.exponent})"


a = SciFloat(1.2, 3)
b = SciFloat(1.2, 3)

print(a * b)
