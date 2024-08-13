from pyasic.miners.backends import AntminerModern
from pyasic.miners.types import S21


class BMMinerS21(AntminerModern, S21):
    stock_nominal_hashrate = [188000, 195000, 200000]
    pass