from math import isclose, floor, log10
from typing import Self

from functools import total_ordering


@total_ordering
class SciFloat:
    """
    SciFloatは、科学的表記法で数値を表現するクラスです。
    mantissaとexponentを持ち、数値の演算をサポートします。
    float誤差を消し飛ばすために、指数を揃えて計算を行います。
    """
    def __init__(self, mantissa: float, exponent: int):
        """SciFloatのコンストラクタ

        Parameters
        ----------
        mantissa : float
            仮数部分
        exponent : int
            指数部分
        """
        self.mantissa = mantissa
        self.exponent = exponent
        self._normalize()

    @classmethod
    def from_float(cls, value: float | int) -> Self:
        """通常の数値からSciFloatインスタンスを生成する"""
        return cls(float(value), 0)

    def _normalize(self):
        if isclose(self.mantissa, 0):
            self.exponent = 0
            return

        power_shift = floor(log10(abs(self.mantissa)))
        self.mantissa /= (10 ** power_shift)
        self.exponent += power_shift

    def _align_exponents(self, other: 'SciFloat') -> tuple[float, float, int]:
        """二つのSciFloatの指数を揃え、調整後の仮数と共通の指数を返す。"""
        exponent = max(self.exponent, other.exponent)
        mantissa1 = self.mantissa * (10 ** (self.exponent - exponent))
        mantissa2 = other.mantissa * (10 ** (other.exponent - exponent))
        return mantissa1, mantissa2, exponent

    def _coerce_other(self, other: object) -> 'SciFloat | None':
        if isinstance(other, (float, int)):
            return type(self).from_float(other)
        if isinstance(other, SciFloat):
            return other
        return None

    def __add__(self, other: object) -> Self:
        other_sci = self._coerce_other(other)
        if other_sci is None:
            return NotImplemented

        m1, m2, exp = self._align_exponents(other_sci)
        return type(self)(m1 + m2, exp)

    def __sub__(self, other: object) -> Self:
        other_sci = self._coerce_other(other)
        if other_sci is None:
            return NotImplemented

        m1, m2, exp = self._align_exponents(other_sci)
        return type(self)(m1 - m2, exp)

    def __mul__(self, other: object) -> Self:
        other_sci = self._coerce_other(other)
        if other_sci is None:
            return NotImplemented

        return type(self)(self.mantissa * other_sci.mantissa, self.exponent + other_sci.exponent)

    def __truediv__(self, other: object) -> Self:
        other_sci = self._coerce_other(other)
        if other_sci is None:
            return NotImplemented

        if isclose(other_sci.mantissa, 0):
            raise ZeroDivisionError("division by zero")

        return type(self)(self.mantissa / other_sci.mantissa, self.exponent - other_sci.exponent)

    __radd__ = __add__
    __rmul__ = __mul__

    def __rsub__(self, other: object) -> Self:
        other_sci = self._coerce_other(other)
        if other_sci is None:
            return NotImplemented
        m1, m2, exp = other_sci._align_exponents(self)
        return type(self)(m1 - m2, exp)

    def __rtruediv__(self, other: object) -> Self:
        other_sci = self._coerce_other(other)
        if other_sci is None:
            return NotImplemented
        if isclose(self.mantissa, 0):
            raise ZeroDivisionError("division by zero")
        return type(self)(other_sci.mantissa / self.mantissa, other_sci.exponent - self.exponent)

    def __eq__(self, other: object) -> bool:
        other_sci = self._coerce_other(other)
        if other_sci is None:
            return NotImplemented

        m1, m2, _ = self._align_exponents(other_sci)
        return isclose(m1, m2)

    def __lt__(self, other: object) -> bool:
        other_sci = self._coerce_other(other)
        if other_sci is None:
            return NotImplemented

        m1, m2, _ = self._align_exponents(other_sci)
        if isclose(m1, m2):
            return False
        return m1 < m2

    def __str__(self):
        return f"{self.mantissa}e{self.exponent}"

    def __repr__(self):
        return f"SciFloat({self.mantissa}, {self.exponent})"

    def __float__(self) -> float:
        return self.mantissa * (10 ** self.exponent)

    def __int__(self) -> int:
        return int(self.__float__())


a = SciFloat(1.2, 3)
b = SciFloat(1.2, 3)

print(a * b)
