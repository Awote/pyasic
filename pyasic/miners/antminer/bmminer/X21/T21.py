from pyasic.miners.backends import AntminerModern
from pyasic.miners.types import T21


class BMMinerT21(AntminerModern, T21):
    stock_nominal_hashrate = [190000]
    pass