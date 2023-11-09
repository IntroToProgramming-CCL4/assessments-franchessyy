age = int(input("Enter the person's age: "))
#if-else elif chain that will print the right text according to the age
if age < 1:
    print("This person is a baby.")
elif age < 5:
    print("This person is a toddler.")
elif age < 11:
    print("This person is a kid.")
elif age < 18:
    print("This person is a teenager.")
elif age < 45:
    print("This person is an adult.")
else:
    print("This person is an elder.")
