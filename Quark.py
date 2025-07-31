from enum import Enum
from dataclasses import dataclass

from SciFloat import SciFloat
from Units import eV, eUnit


@dataclass(frozen=True)
class QuarkProperty:
    charge: SciFloat
    mass: SciFloat
    gen: int


class Flavor(Enum):
    UP = QuarkProperty(charge=SciFloat(2, 0) / SciFloat(3, 0), mass=SciFloat(2.2, 6), gen=1)
    DOWN = QuarkProperty(charge=SciFloat(-1, 0) / SciFloat(3, 0), mass=SciFloat(4.7, 6), gen=1)
    CHARM = QuarkProperty(charge=SciFloat(2, 0) / SciFloat(3, 0), mass=SciFloat(1.27, 9), gen=2)
    STRANGE = QuarkProperty(charge=SciFloat(-1, 0) / SciFloat(3, 0), mass=SciFloat(96, 6), gen=2)
    TOP = QuarkProperty(charge=SciFloat(2, 0) / SciFloat(3, 0), mass=SciFloat(173.1, 9), gen=3)
    BOTTOM = QuarkProperty(charge=SciFloat(-1, 0) / SciFloat(3, 0), mass=SciFloat(4.18, 9), gen=3)

    @property
    def charge(self) -> SciFloat:
        return self.value.charge

    @property
    def mass(self) -> SciFloat:
        return self.value.mass

    @property
    def gen(self) -> int:
        return self.value.gen


class Spin(Enum):
    UP = SciFloat(0.5, 0)
    DOWN = SciFloat(-0.5, 0)


class Color(Enum):
    RED = "red"
    GREEN = "green"
    BLUE = "blue"


@dataclass(frozen=True)
class Quark:
    """
    素粒子であるクォークを表現するクラス。

    Attributes
    ----------
    flavor : Flavor
        クォークのフレーバー (UP, DOWNなど)。
    color : Color
        クォークの色荷 (RED, GREEN, BLUE)。
    spin : Spin
        クォークのスピン (UP, DOWN)。
    """

    flavor: Flavor
    color: Color
    spin: Spin

    @property
    def charge(self) -> eUnit:
        """クォークの電荷を返す。"""
        return eUnit(self.flavor.charge)

    @property
    def mass(self) -> eV:
        """クォークの質量を返す。"""
        return eV(self.flavor.mass)

    @property
    def gen(self) -> int:
        """クォークの世代を返す。"""
        return int(self.flavor.gen)

    def __str__(self) -> str:
        return f"Quark(flavor={self.flavor.name}, color={self.color}, spin={self.spin.name})"
