from enum import Enum
from typing import Literal, Tuple
from dataclasses import dataclass

from SciFloat import SciFloat


class Flavor(Enum):
    UP = "up"
    DOWN = "down"
    CHARM = "charm"
    STRANGE = "strange"
    TOP = "top"
    BOTTOM = "bottom"


class Spin(Enum):
    UP = SciFloat(5, -1)
    DOWN = SciFloat(-5, -1)


class Color(Enum):
    RED = "red"
    GREEN = "green"
    BLUE = "blue"


@dataclass
class Quark:
    flavor: Flavor
    color: Color
    spin: Spin
    charge: SciFloat
    position: Tuple[SciFloat, SciFloat, SciFloat]
    gen: Literal[1, 2, 3]
