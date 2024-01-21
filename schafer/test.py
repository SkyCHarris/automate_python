names = ['Peter Parker', 'Clark Kent', 'Wade Wilson', 'Bruce Wayne']
heroes = ['Spiderman', 'Superman', 'Deadpool', 'Batman']

identities = list(zip(names, heroes))   # convert to list from the start

print(identities)

for identity in identities:
    print('{} is actually {}!'. format(identity[0], identity[1]))