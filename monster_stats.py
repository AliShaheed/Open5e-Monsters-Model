from monster_endpoint_model import BasicsModel
import requests

class BasicStats():
    def __init__(self, monster) -> None:  # initialisation monster data from open5e
        self.url = f'https://api.open5e.com/monsters/{monster}'
        self.response = requests.get(self.url)
        self.monster_data = self.response.json() # format to json

    def get_stats(self):
        return BasicsModel(self.monster_data) # return modelled stats