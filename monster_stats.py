from monster_basics_model import BasicsModel
from monster_abilities_model import AbilitiesModel
import requests

class Stats():
    def __init__(self, monster) -> None:  # initialisation monster data from open5e
        self.url = f'https://api.open5e.com/monsters/{monster}'
        self.response = requests.get(self.url)
        self.monster_data = self.response.json() # format to json

    def get_stats(self, type: str):
        """
        type options: 'basic', 'ability' 
        """
        match type:
            case 'basic':
                return BasicsModel(self.monster_data) # return modelled stats
            case 'ability':
                return AbilitiesModel(self.monster_data)
            case _:
                return "Unknown argument!"