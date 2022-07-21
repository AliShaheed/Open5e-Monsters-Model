from monster_stats import BasicStats

monster = BasicStats('adult-black-dragon') # pass monster name (needs to be hyphenated) into model

monster_stats = monster.get_stats() # store stats as attributes of monster_status object

print(monster_stats.name) # print name attribute, returns 'Adult Black Dragon'
