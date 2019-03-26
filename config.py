import configparser


class ConfigLoader:
    config_file = ""

    def __init__(self, config_file="config.ini"):
        self.config_file = config_file

        self._load_configs()

    def _load_configs(self):
        pass
