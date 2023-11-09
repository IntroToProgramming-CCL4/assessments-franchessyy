# Make an empty list to store the pets in.
pets = []

# Make individual pets, and store each one in the list.
pet = {
    'animal type': 'dog',
    'name': 'marikit',
    'owner': 'kisha',
    'weight': 5.2,
    'eats': 'dog food',
}
pets.append(pet)

pet = {
    'animal type': 'cat',
    'name': 'tofu',
    'owner': 'albert',
    'weight': 4.1,
    'eats': 'cat food',
}
pets.append(pet)

pet = {
    'animal type': 'dog',
    'name': 'money',
    'owner': 'kisha',
    'weight': 10,
    'eats': 'dog food',
}
pets.append(pet)

# Display information about each pet.
for pet in pets:
    print("\nEverything I know about " + pet['name'].title() + ":")
    for key, value in pet.items():
        print("\t" + key + ": " + str(value))