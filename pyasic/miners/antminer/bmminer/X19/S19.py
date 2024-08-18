# ------------------------------------------------------------------------------
#  Copyright 2022 Upstream Data Inc                                            -
#                                                                              -
#  Licensed under the Apache License, Version 2.0 (the "License");             -
#  you may not use this file except in compliance with the License.            -
#  You may obtain a copy of the License at                                     -
#                                                                              -
#      http://www.apache.org/licenses/LICENSE-2.0                              -
#                                                                              -
#  Unless required by applicable law or agreed to in writing, software         -
#  distributed under the License is distributed on an "AS IS" BASIS,           -
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.    -
#  See the License for the specific language governing permissions and         -
#  limitations under the License.                                              -
# ------------------------------------------------------------------------------

from pyasic.miners.backends import AntminerModern
from pyasic.miners.types import (
    S19,
    S19L,
    S19XP,
    S19a,
    S19aPro,
    S19i,
    S19j,
    S19jNoPIC,
    S19jPro,
    S19Plus,
    S19Pro,
    S19ProHydro,
    S19ProPlus,
    S19kPro,
    S19Hydro,
    S19ProPlusHydro,
    S19XPHydro,
    S19jProA,
    S19jProPlus,
    S19jXP,
    S19kProNoPIC,
    S19NoPIC,
)


class BMMinerS19(AntminerModern, S19):
    stock_nominal_hashrate = [82, 86, 90, 92, 95]
    pass


class BMMinerS19Plus(AntminerModern, S19Plus):
    pass


class BMMinerS19i(AntminerModern, S19i):
    pass


class BMMinerS19Pro(AntminerModern, S19Pro):
    stock_nominal_hashrate = [100, 104, 105, 110, 92, 96]
    pass


class BMMinerS19ProPlus(AntminerModern, S19ProPlus):
    pass


class BMMinerS19XP(AntminerModern, S19XP):
    stock_nominal_hashrate = [119, 127, 134, 141, 140, 151]
    pass


class BMMinerS19a(AntminerModern, S19a):
    stock_nominal_hashrate = [88, 92, 96, 100]
    pass


class BMMinerS19aPro(AntminerModern, S19aPro):
    stock_nominal_hashrate = [102, 106, 110]
    pass


class BMMinerS19j(AntminerModern, S19j):
    stock_nominal_hashrate = [82, 86, 90, 94, 100]
    pass


class BMMinerS19jNoPIC(AntminerModern, S19jNoPIC):
    pass


class BMMinerS19jPro(AntminerModern, S19jPro):
    stock_nominal_hashrate = [100, 104, 84, 88, 92, 96, 98]
    pass


class BMMinerS19L(AntminerModern, S19L):
    pass


class BMMinerS19ProHydro(AntminerModern, S19ProHydro):
    stock_nominal_hashrate = [154.5, 162, 163, 169.5, 170, 177, 184]
    pass


class BMMinerBHB42621(BMMinerS19jPro):
    pass


class BMMinerS19kPro(AntminerModern, S19kPro):
    stock_nominal_hashrate = [110, 115, 120]
    pass


class BMMinerS19Hydro(AntminerModern, S19Hydro):
    stock_nominal_hashrate = [132, 138.5, 145, 151.5, 158]
    pass


class BMMinerS19ProPlusHydro(AntminerModern, S19ProPlusHydro):
    stock_nominal_hashrate = [170, 177, 184, 191, 198]
    pass


class BMMinerS19XPHydro(AntminerModern, S19XPHydro):
    stock_nominal_hashrate = [224, 235, 246, 255, 257]
    pass

class BMMinerS19jProA(AntminerModern, S19jProA):
    stock_nominal_hashrate = [84, 88, 92, 96, 100, 104, 113]
    pass

class BMMinerS19jProPlus(AntminerModern, S19jProPlus):
    stock_nominal_hashrate = [113, 109, 117, 120]
    pass    

class BMMinerS19jXP(AntminerModern, S19jXP):
    stock_nominak_hashrate = [134, 136 ,139, 143, 151]
    pass

class BMMinerS19kProNoPIC(AntminerModern, S19kProNoPIC):
    pass

class BMMinerS19NoPIC(AntminerModern, S19NoPIC):
    pass