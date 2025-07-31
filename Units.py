from typing import Final, NewType

from SciFloat import SciFloat

# --- 物理定数 (単位なしのSciFloat) ---
_e_charge_in_coulombs_val = SciFloat(1.602176634, -19)
_h_bar_in_Js_val = SciFloat(1.054571817, -34)
_c_in_ms_val = SciFloat(299792458, 0)


# --- 単位型の定義 ---
# NewTypeを使って、それぞれの物理量を区別する「型」を作る
Coulomb = NewType('Coulomb', SciFloat)                  # 電荷の単位
Joule = NewType('Joule', SciFloat)                      # エネルギーの単位
JouleSecond = NewType('JouleSecond', SciFloat)          # 角運動量の単位
Meter = NewType('Meter', SciFloat)                      # 長さの単位
Second = NewType('Second', SciFloat)                    # 時間の単位
MeterPerSecond = NewType('MeterPerSecond', SciFloat)    # 速度の単位

eUnit = NewType('eUnit', SciFloat)                      # 電荷の単位（e単位）

eV = NewType('eV', SciFloat)                            # electron volt (1eV=1.602176634e-19 J)


E_CHARGE: Final[Coulomb] = Coulomb(_e_charge_in_coulombs_val)
H_BAR: Final[JouleSecond] = JouleSecond(_h_bar_in_Js_val)
C: Final[MeterPerSecond] = MeterPerSecond(_c_in_ms_val)

# --- 単位変換係数 ---
EV_TO_JOULE: Final[SciFloat] = _e_charge_in_coulombs_val
