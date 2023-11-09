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

# Mathilda can't make it to dinner! Let's invite Alson instead.
del(guests[1])
guests.insert(1, 'Alson Ocampo')

# Print second set of invitations again.
name = guests[0].title()
print("\n" + name + ", Hi! I would like to have a dinner with you.")

name = guests[1].title()
print(name + ", Hi! I would like to have a dinner with you.")

name = guests[2].title()
print(name + ", Hi! I would like to have a dinner with you.")