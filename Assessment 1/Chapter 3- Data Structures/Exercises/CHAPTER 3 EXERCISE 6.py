# Invite some people to dinner.
guests = ['Albert Alfonso', 'Mathilda Labao', 'Nabeel Hamza']

name = guests[0].title()
print(name + ", Hi! I would like to have a dinner with you.")

name = guests[1].title()
print(name + ", Hi! I would like to have a dinner with you.")

name = guests[2].title()
print(name + ", Hi! I would like to have a dinner with you.")

name = guests[1].title()
print("\nSorry, " + name + " can't make it to dinner.")

# Mathilda can't make it! Let's invite Alson instead.
del(guests[1])
guests.insert(1, 'Alson Ocampo')

# Print second set of the invitations again.
name = guests[0].title()
print("\n" + name + ", Hi! I would like to have a dinner with you.")

name = guests[1].title()
print(name + ", Hi! I would like to have a dinner with you.")

name = guests[2].title()
print(name + ", Hi! I would like to have a dinner with you.")

# Oh no, the table won't arrive on time!
print("\nSorry, we can only invite two people to dinner.")

name = guests[0].title()
print("Sorry, " + name.title() + " there's no room at the table.")

name = guests[1].title()
print("Sorry, " + name.title() + " there's no room at the table.")

name = guests[2].title()
print("Sorry, " + name.title() + " there's no room at the table.")


# There should be two people left. Let's invite them.
name = guests[0].title()
print(name + ", Hi! I would like to have a dinner with you there's still room available at the table.")

name = guests[2].title()
print(name + ", Hi! I would like to have a dinner with you there's still room available at the table.")

# Empty out the list.
del(guests[0])
del(guests[0])
del(guests[0])

# Prove the list is empty.
print(guests)


