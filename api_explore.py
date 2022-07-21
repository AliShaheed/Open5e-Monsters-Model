"""
# api_explore
# Exploration of Open5e Monsters data structre
# by Ali Shaheed
"""
import requests

url = 'https://api.open5e.com/monsters/adult-black-dragon'
response = requests.get(url)
monster_data = response.json()

for data in monster_data:
    print(data,':', monster_data[data])


print(len(monster_data))
