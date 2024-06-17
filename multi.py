
import sys
import json

filtered_file = sys.argv[1]
n = sys.argv[2]


# convert file to list
bracket_file = 'brackets_prob.json'

bprobs = list(bracket_file.values())
bprob = bprobs[n] # podemos comprobar que esta n se corresponde con la misma lista de teams de teams_n.ini

winprob_file = 'win_prob.json'
with open(winprob_file, 'r') as file:
    winprob = json.load(file)

with open(filtered_file, 'r') as f:
    head = f.readline()
    for line in f: 
        fields = line.strip().split(',')
        team = fields[1]
        prob = fields[2]
        winprob[team] = bprob * prob

with open(winprob_file, 'w') as file:
    json.dump(winprob, file, indent=4)


    



