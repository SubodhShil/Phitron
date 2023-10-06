person = {
    'name': 'Subodh',
    'age': 23
}

print(person)
print(person['age'])

# Shows the key of the dictionary
print(person.keys())

# Shows the key of the dictionary
print(person.values())

# delete an item
del person['age']
print(person)
print(len(person))

# looping a dictionary
for key, value in person.items():
    print(key, value)
