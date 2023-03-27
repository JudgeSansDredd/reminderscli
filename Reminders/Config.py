from configparser import ConfigParser
from pathlib import Path

from gui.whiptail import wt

CONFIG_PATH = Path(f'{Path.home()}/.reminderscli/config.ini')

class Config:
    def __init__(self):
        self.config = ConfigParser()
        self.config.read(CONFIG_PATH)

    def _set_configuration(self):
        configItems = {
            "REMINDERS": [
                "DEFAULT_LIST",
            ],
        }

        # Set up config and prompt if needed
        for section, options in configItems.items():
            if not self.config.has_section(section):
                self.config.add_section(section)
            for option in options:
                if not self.config.has_option(section, option):
                    default = "Reminders" if option == "DEFAULT_LIST" else ""
                    value, response = wt.inputbox(f"Enter value for: {option}", default)
                    if response == 1:
                        return False
                    self.config.set(section, option, value)

        # Make sure the .reminderscli directory exists
        CONFIG_PATH.parents[0].mkdir(parents=True, exist_ok=True)
        with open(CONFIG_PATH, 'w', encoding="UTF-8") as conf:
            self.config.write(conf)

        return True

    @classmethod
    def set_configuration(cls) -> bool:
        return cls()._set_configuration()

    def _get_default_list(self) -> str:
        return self.config.get('REMINDERS', 'DEFAULT_LIST')

    @classmethod
    def get_default_list(cls):
        return cls()._get_default_list()
