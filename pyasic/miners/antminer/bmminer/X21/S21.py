from pyasic.miners.backends import AntminerModern
from pyasic.miners.types import S21, S21Hydro, S21Pro, S21XP, S21XPIMM


class BMMinerS21(AntminerModern, S21):
    stock_nominal_hashrate = [188, 195, 200]
    pass

class BMMinerS21Hydro(AntminerModern, S21Hydro):
    stock_nominal_hashrate = [302, 319, 335]
    pass

class BMMinerS21Pro(AntminerModern, S21Pro):
    stock_nominal_hashrate = [234]
    pass

class BMMinerS21XP(AntminerModern, S21XP):
    stock_nominal_hashrate = [270]
    pass

class BMMinerS21XPIMM(AntminerModern, S21XPIMM):
    stock_nominal_hashrate = [270]
    pass