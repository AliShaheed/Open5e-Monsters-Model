from numpy import size
from torch import _cudnn_rnn_flatten_weight


class BasicsModel:
    def __init__(self, monster) -> None:
        self.name = monster['name']
        self.size = monster['size']
        self.group = monster['group']
        self.type = monster['type']
        self.alignment = monster['alignment']
        self.ac = monster['armor_class']
        self.armour_desc = monster['armor_desc']
        self.hp = monster['hit_points']
        self.hp_dice = monster['hit_dice']
        self.speed = monster['speed']
        self.base_stats = {'strengh': monster['strength'], 
                           'dexterity': monster['dexterity'],
                           'constitution': monster['constitution'],
                           'intelligence': monster['intelligence'],
                           'wisdom': monster['wisdom'],
                           'charisma': monster['charisma']}
        self.challenge_rating = monster['challenge_rating']
