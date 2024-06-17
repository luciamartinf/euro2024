
import json

elo = {'France': 2077, 'Spain': 2020, 'Portugal': 2001, 'Belgium': 1988, 'England': 1981, 'Netherlands': 1974, 'Croatia': 1969, 'Italy': 1950, 'Germany': 1920, 'Austria': 1863, 'Ukraine': 1850, 'Denmark': 1834, 'Hungary': 1832, 'Switzerland': 1805, 'Serbia': 1801, 'Czech Republic': 1777, 'Scotland': 1770, 'Turkey': 1749, 'Poland': 1746, 'Slovenia': 1733, 'Slovakia': 1671, 'Georgia': 1666, 'Romania': 1647, 'Albania': 1624}

teams = list(elo.keys())


win_prob = {}

for t in teams: 
    win_prob[t] = []

print(win_prob)

with open('win_prob.json', 'w') as file:
    json.dump(win_prob, file, indent=4)