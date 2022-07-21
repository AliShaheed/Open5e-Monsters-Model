# Open5e-Monsters-Model
A Dungeons &amp; Dragon (5e) Monsters Model using Open5e

## Open5e API
The Open5e API provides programmatic access to all resources and rules included on this site.
Open5e API's documentation can be found [here](https://open5e.com/api-docs)

## Test Monster
For modelling monster statistics, the stat block for the [Adult Black Dragon](https://open5e.com/monsters/adult-black-dragon) was used. Exporation code the stat block structure can be found in `api_explore.py`. The data was in a single json format, each stat its own key-value pair - other actions and legendary actions. Some initital basic stats were added as their on model. Other models can be added, for skills, actions, legendary actions, etc... might be a possibly approach to create a simple and easy api exposing data of interest.