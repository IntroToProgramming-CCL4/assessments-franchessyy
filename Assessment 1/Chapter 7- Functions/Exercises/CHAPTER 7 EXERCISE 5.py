#print 3 countries and its city together! 
def describe_city(city, country='philippines'):
    """Describe a city."""
    msg = city.title() + " is in " + country.title() + "."
    print(msg)

describe_city('Makati')
describe_city('San fransisco California', 'USA')
describe_city('Taguig')