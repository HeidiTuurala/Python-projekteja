import operator

ages = {'Mirjami':35, 'Matti':55, 'Riikka':28}
print(type(ages))

def add_to_dict(name, age, ages):
    ages[name] = age
    return ages

ages = {'Mirjami':35, 'Matti':55, 'Riikka':28}
add_to_dict('Jukka', 41, ages)
print(ages)

print(ages.get('Marko'))