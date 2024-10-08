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

from pyasic.miners.backends import AntminerOld
from pyasic.miners.types import T17, T17e, T17Plus


class BMMinerT17(AntminerOld, T17):
    stock_nominal_hashrate = [42000]
    pass


class BMMinerT17Plus(AntminerOld, T17Plus):
    stock_nominal_hashrate = [58000]
    pass


class BMMinerT17e(AntminerOld, T17e):
    stock_nominal_hashrate = [53000]
    pass
