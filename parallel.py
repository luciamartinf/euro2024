import json

file = 'brackets_prob.json'
with open(file, 'r') as file:
    brackets = json.load(file)

length = len(list(brackets.keys()))

with open('parallelize_phylourny.txt', 'w') as f:
    for n in range(length): 
        command = f'phylourny --teams teams_{n}.ini --matches matches.ini --prefix bracket_{n} --samples 1000 --burnin 100 ; filter.py --results  bracket_{n}.dynamic.samples.json --output  bracket_{n}.filtered.csv --field win_prob --teams  bracket{n}_.dynamic.teams.json ; multi.py bracket_{n}.filtered.csv {n}\n'
        f.write(command)