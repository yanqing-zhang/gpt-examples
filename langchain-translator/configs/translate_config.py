import yaml


class TranslationConfig:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(TranslationConfig, cls).__new__(cls)
            cls._instance._config = None
        return cls._instance

    def initialize(self):
        with open("./application.yaml", "r") as f:
            config = yaml.safe_load(f)

    def __getattr__(self, name):
        if self._instance._config and name in self._instance._config:
            return self._instance._config[name]
        raise AttributeError(f"'TranslationConfig' object has no attribute '{name}'")