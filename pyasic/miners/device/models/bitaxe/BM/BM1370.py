from pyasic.device.algorithm import MinerAlgo
from pyasic.device.models import MinerModel
from pyasic.miners.device.makes import BitAxeMake


class Gamma(BitAxeMake):
    raw_model = MinerModel.BITAXE.BM1370

    expected_hashboards = 1
    expected_chips = 1
    expected_fans = 1
    algo = MinerAlgo.SHA256
