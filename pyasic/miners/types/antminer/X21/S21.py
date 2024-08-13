from pyasic.miners.makes import AntMiner

class S21(AntMiner):  # noqa - ignore ABC method implementation
    def __init__(self, ip: str, api_ver: str = "0.0.0"):
        super().__init__(ip, api_ver)
        self.ip = ip
        self.model = "Antminer S21"
        self.expected_chips = 108
        self.fan_count = 4

class S21Hydro(AntMiner):  # noqa - ignore ABC method implementation
    def __init__(self, ip: str, api_ver: str = "0.0.0"):
        super().__init__(ip, api_ver)
        self.ip = ip
        self.model = "Antminer S21 Hyd."
        self.expected_chips = 216
        self.fan_count = 0