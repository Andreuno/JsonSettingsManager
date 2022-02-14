import json

# For devoltage use:
# config = Settings()
#
# Using your path to json file:
# Settings.path_config = "config_file.json"
# config = Settings()

# =========================================================== CLASSES

class Settings():
    """ Auto convert json config file to class attributes.
    Auto-update json config file from class attributes."""

    path_config = "config.json"

    def __init__(self):
        with open(self.path_config) as json_file:
            self.__dict__.update(json.load(json_file))

    def __setattr__(self, name, value):
        self.__dict__[name] = value
        self.save()

    def __delattr__(self, name):
        del self.__dict__[name]
        self.save()

    def save(self):
        # Saving all class attributes in json config file
        with open(self.path_config, "w") as f:
            json.dump(self.__dict__, f, sort_keys=True, indent=4)
