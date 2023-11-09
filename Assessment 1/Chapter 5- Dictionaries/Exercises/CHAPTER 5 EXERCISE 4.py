#print the river with their locations 
rivers = {
    'rio grande': 'united states',
    'amazon river': 'united states',
    'orange river': 'south africa',
    'xijiang river': 'china',
    'godavari river': 'india',
    }

for river, country in rivers.items():
    print("The " + river.title() + " runs through " + country.title() + ".")

print("\nThe following rivers are included in this data set:")
for river in rivers.keys():
    print("- " + river.title())

print("\nThe following countries are included in this data set:")
for country in rivers.values():
    print("- " + country.title())
