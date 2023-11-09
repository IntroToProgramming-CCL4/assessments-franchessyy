
prompt = "How old are you?"
prompt += "\nEnter 'quit' when you are finished. "

while True:
    age = input(prompt)
    if age == 'quit':
        break
    age = int(age)

    #if you're 3 below..
    if age < 3:
        print("  You get in free!")
    #if you're 12 below ..
    elif age < 13:
        print("  Your ticket is $10.")
    #if you're 18 above..
    else:
        print("  Your ticket is $15.")