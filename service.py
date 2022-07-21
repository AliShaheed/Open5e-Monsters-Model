from monster_stats import Stats

monster = Stats('adult-black-dragon') # pass monster name (needs to be hyphenated) into model

monster_basic = monster.get_stats('basic') # store stats as attributes of monster_status object
monster_abilities =  monster.get_stats('ability')

print(monster_basic.name) # print name attribute, returns 'Adult Black Dragon'
print(monster_abilities.special_abilities) # print special_abilities attribute, returns list of dictionaries
