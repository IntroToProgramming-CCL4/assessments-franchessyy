favorite_fruits = []

#  will enter their 3 favorite fruits
for i in range(3):
    fruit = input(f"Enter your favorite fruit {i+1}: ")
    favorite_fruits.append(fruit.lower())  

# Check if the the favourite fruits are in here
if "mango" in favorite_fruits:
    print("Great! You really like mangoes!")

if "apple" in favorite_fruits:
    print("Great! You really like apples!")

if "grapes" in favorite_fruits:
    print("Great! You really like grapes!")

if "dragonfruit" in favorite_fruits:
    print("Great! You really like dragonfruit!")

if "banana" in favorite_fruits:
    print("Great! You really like banana!")
