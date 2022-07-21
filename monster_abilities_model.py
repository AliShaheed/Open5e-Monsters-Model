class AbilitiesModel:
    def __init__(self, monster) -> None:
        self.saving_throws = {'strength_save': monster['strength_save'],
                              'dexterity_save': monster['dexterity_save'],
                              'constitution_save': monster['constitution_save'],
                              'intelligence_save': monster['intelligence_save'],
                              'wisdom_save': monster['wisdom_save'],
                              'charisma_save': monster['charisma_save']}
        self.skills = monster['skills']
        self.damage_immunities = monster['damage_immunities']
        self.sense = monster['senses']
        self.languages = monster['languages']
        self.special_abilities = monster['special_abilities']