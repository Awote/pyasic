from pyasic.miners.backends import AntminerModern
from pyasic.miners.types import S21, S21Hydro, S21Pro, S21XP, S21XPIMM


class BMMinerS21(AntminerModern, S21):
    stock_nominal_hashrate = [188000, 195000, 200000]
    pass

class BMMinerS21Hydro(AntminerModern, S21Hydro):
    stock_nominal_hashrate = [302000, 319000, 335000]
    pass

class BMMinerS21Pro(AntminerModern, S21Pro):
    stock_nominal_hashrate = [234000]
    pass

class BMMinerS21XP(AntminerModern, S21XP):
    stock_nominal_hashrate = [270000]
    pass

class BMMinerS21XPIMM(AntminerModern, S21XPIMM):
    stock_nominal_hashrate = [270000]
    pass