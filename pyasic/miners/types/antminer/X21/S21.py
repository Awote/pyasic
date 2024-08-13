from pyasic.miners.makes import AntMiner

class S21(AntMiner):  # noqa - ignore ABC method implementation
    def __init__(self, ip: str, api_ver: str = "0.0.0"):
        super().__init__(ip, api_ver)
        self.ip = ip
        self.model = "S21"
        self.expected_chips = 108
        self.fan_count = 4

class S21Hydro(AntMiner):  # noqa - ignore ABC method implementation
    def __init__(self, ip: str, api_ver: str = "0.0.0"):
        super().__init__(ip, api_ver)
        self.ip = ip
        self.model = "S21 Hydro"
        self.expected_chips = 216
            # TODO check is correct
        self.fan_count = 0

class S21Pro(AntMiner):  # noqa - ignore ABC method implementation
    def __init__(self, ip: str, api_ver: str = "0.0.0"):
        super().__init__(ip, api_ver)
        self.ip = ip
        self.model = "S21 Pro"
        self.expected_chips = 65
        self.fan_count = 4

class S21XP(AntMiner):  # noqa - ignore ABC method implementation
    def __init__(self, ip: str, api_ver: str = "0.0.0"):
        super().__init__(ip, api_ver)
        self.ip = ip
        self.model = "S21 XP"
        self.expected_chips = 108
        self.fan_count = 4

class S21XPIMM(AntMiner):  # noqa - ignore ABC method implementation
    def __init__(self, ip: str, api_ver: str = "0.0.0"):
        super().__init__(ip, api_ver)
        self.ip = ip
        self.model = "S21 XP IMM"
        self.expected_chips = 108
        self.fan_count = 4

class S21XPHydro(AntMiner):
    def __init__(self, ip: str, api_ver: str = "0.0.0"):
        super().__init__(ip, api_ver)
        self.ip = ip
        self.model = "S21 XP Hydro"
        self.expected_chips = 108
        self.fan_count = 0