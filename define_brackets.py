#!/opt/homebrew/bin/python3

import ast
import json

file = 'all_brackets.txt'

elo_ranking = {'France': 2077, 'Spain': 2020, 'Portugal': 2001, 'Belgium': 1988, 'England': 1981, 'Netherlands': 1974, 'Croatia': 1969, 'Italy': 1950, 'Germany': 1920, 'Austria': 1863, 'Ukraine': 1850, 'Denmark': 1834, 'Hungary': 1832, 'Switzerland': 1805, 'Serbia': 1801, 'Czech Republic': 1777, 'Scotland': 1770, 'Turkey': 1749, 'Poland': 1746, 'Slovenia': 1733, 'Slovakia': 1671, 'Georgia': 1666, 'Romania': 1647, 'Albania': 1624}
template = [(1,['B']), (3,['A','D','E','F']), 
           (1,['A']), (2,['C']), 
           (1,['F']), (3,['A','B','C']), 
           (2,['D']), (2,['E']), 
           (1,['E']), (3,['A','B','C','D']),
           (1,['D']), (2,['F']),
           (1,['C']), (3,['D','E','F']),
           (2,['A']), (2,['B'])]

ranking = list(elo_ranking.keys())
groups = ['A', 'B', 'C', 'D', 'E', 'F']
thirds_dict = {'ABCD': ['A', 'C', 'B', 'D'], 'ABCE': ['A', 'C', 'B', 'E'], 'ABCF': ['A', 'C', 'B', 'F'], 'ABDE': ['D', 'B', 'A', 'E'], 'ABDF': ['D', 'B', 'A', 'F'], 'ABEF': ['E', 'A', 'B', 'F'], 'ACDE': ['E', 'A', 'C', 'D'], 'ACDF': ['F', 'A', 'C', 'D'], 'ACEF': ['E', 'A', 'C', 'F'], 'ADEF': ['E', 'A', 'D', 'F'], 'BCDE': ['E', 'C', 'B', 'D'], 'BCDF': ['F', 'B', 'C', 'D'], 'BCEF': ['F', 'B', 'C', 'E'], 'BDEF': ['F', 'B', 'D', 'E'], 'CDEF': ['F', 'C', 'D', 'E']}


def write_json(dict, filename):
    with open(filename, 'w') as json_file:
        json.dump(dict, json_file, indent=4)

def add_value(dict, key, value):

    if not key in dict.keys():
        dict[key] = value
    else: 
        dict[key] += value
    return dict


with open(file, 'r') as f:
    teams_ini = {}
    for line in f: 
        bracket = {}
        thirds = {}
        teams_list = []
        # Split the line to separate the tuple and the number
        tuple_str, probability_str = line.split(") ", 1)
        tuple_str += ")"

        # Use ast.literal_eval to safely evaluate the tuple part
        tuple_value = ast.literal_eval(tuple_str)
        for g, t in enumerate(tuple_value):
            t_list = list(t)
            bracket[groups[g]] = t_list
            thirds[groups[g]] = [elo_ranking[t_list[-1]], t_list[-1]] 

        sorted_thirds = dict(sorted(thirds.items(), key=lambda item: item[1][0], reverse=True)[:4])

        top_thirds = dict(sorted(sorted_thirds.items()))
        top_thirds = ''.join(list(top_thirds.keys()))

        bracket_list = []
        
        order = thirds_dict[top_thirds].copy()
        for position in template:
            posit = position[0]
            if posit == 3:
                group = order[0]
                
                order.remove(group)
                
            else:
                group = position[1][0]
            
            team = bracket[group][posit-1]  
        
            teams_list.append(team)

        
        # Optionally, convert the probability to a float
        probability_value = float(probability_str)

        teams_ini = add_value(teams_ini, tuple(teams_list), probability_value)


write_json(teams_ini, 'brackets_prob.json')

n = 0
for bracket, prob in teams_ini.items():

    team_file = f'teams_{n}.ini'

    with open(team_file, 'w') as f:
        for t in bracket:
            f.write(f'{t}\n')

    n+=1 

