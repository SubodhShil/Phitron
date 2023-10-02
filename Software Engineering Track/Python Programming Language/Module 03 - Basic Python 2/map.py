double = lambda x : x * 2

numList = [21, 12, 33, 55, 29, 70]
# doubled_values = list(map(double, numList))

# map: iterate over all the values of the list
doubled_values = list(map(lambda x : x * 2, numList))
print(numList)
print(doubled_values)


actors = [
    {'name' : 'Modoska Kraklon', 'cnt': 1},
    {'age': '-∞', 'cnt': 2},
    {'occupation': 'destroy goofy', 'cnt': 3},
    {'likes' : 'everything', 'cnt':4}, 
    {'dislikes': 'everything', 'cnt': 5}
]


# filter: works for every element in the list
more_values = list(filter(lambda actor : actor['cnt'] <= 4, actors))
print(more_values)