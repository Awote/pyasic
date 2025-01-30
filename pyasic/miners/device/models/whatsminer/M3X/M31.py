from pyasic.device.algorithm import MinerAlgo
from pyasic.device.models import MinerModel
from pyasic.miners.device.makes import WhatsMinerMake


class M31V10(WhatsMinerMake):
    raw_model = MinerModel.WHATSMINER.M31V10

    expected_chips = 70
    expected_fans = 2
    expected_hashboards = 3
    algo = MinerAlgo.SHA256


class M31V20(WhatsMinerMake):
    raw_model = MinerModel.WHATSMINER.M31V20

    expected_chips = 74
    expected_fans = 2
    expected_hashboards = 3
    algo = MinerAlgo.SHA256
