people = [
    {'name': 'Harry', 'house': 'Gryffindor'},
    {'name': 'Cho', 'house': 'Ravenclaw'},
    {'name': 'Draco', 'house': 'Slytherin'},
]

# # Sort by houses
# def f(person):
#     return person['house']

# # Sort by names 
# def f(person):
#     return person['name']

# people.sort(key = f)

people.sort(key = lambda person: person['name'])
people.sort(key = lambda person: person['house'])

print(people)