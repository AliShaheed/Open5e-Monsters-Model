from monster_endpoint_model import BasicsModel
import requests

class BasicStats():
    def __init__(self, monster) -> None:
        self.url = f'https://api.open5e.com/monsters/{monster}'
        self.response = requests.get(self.url)
        self.monster_data = self.response.json()

    def get_stats(self):
        return BasicsModel(self.monster_data)