# ------------------------------------------------------------------------------
#  Copyright 2023 Upstream Data Inc                                            -
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

from pyasic.miners.backends import M6X
from pyasic.miners.types import M63VK10, M63VK20, M63VK30


class BTMinerM63VK10(M6X, M63VK10):
    pass


class BTMinerM63VK20(M6X, M63VK20):
    pass


class BTMinerM63VK30(M6X, M63VK30):
    pass
