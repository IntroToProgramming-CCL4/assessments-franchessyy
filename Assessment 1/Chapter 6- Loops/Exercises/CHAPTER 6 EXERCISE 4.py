#toppings of the sandwich
sandwich_orders = ['lettuce', 'grilled cheese', 'grilled chicken', 'bacon']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I'm working on your " + current_sandwich + " sandwich.")
    finished_sandwiches.append(current_sandwich)
#this will print out the finish product
print("\n")
for sandwich in finished_sandwiches:
    print("I made a " + sandwich + " sandwich.")