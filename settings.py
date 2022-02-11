import json

# =========================================================== CLASSES

class Settings():
    def __init__(self):
        self.file = 'config.json'
        with open(self.file) as json_file:
            self.data = json.load(json_file)

    def __getattr__(self, name):
        if name in self.data:
            if name in self.__dict__:
                return self.__dict__[name]
            else:
                self.__dict__[name] = self.data[name]
                return self.__dict__[name]
        else:
            raise AttributeError(f'Settings() has not atribute "{name}."')

    def _data(self, name, value):
        self.data[name] = value
        self.save()

    def save(self):
        with open(self.file, "w") as f:
            json.dump(self.data, f, sort_keys=True, indent=4)



# =========================================================== MAIN
