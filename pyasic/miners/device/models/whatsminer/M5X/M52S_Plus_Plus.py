from pyasic.device.algorithm import MinerAlgo
from pyasic.device.models import MinerModel
from pyasic.miners.device.makes import WhatsMinerMake


class M52SPlusPlusVL10(WhatsMinerMake):
    raw_model = MinerModel.WHATSMINER.M52SPlusPlusVL10

    expected_chips = 87
    expected_fans = 0
    expected_hashboards = 4
    algo = MinerAlgo.SHA256
