alien_color = input("Enter the color of the alien: ")
#if green
if alien_color == "green":
    print("Wow! Congratulations you just earned 5 points!")
#if yellow
elif alien_color == "yellow":
    print("Wow! You just earned 10 points!")
#if red
elif alien_color == "red":
    print("Wow! Congratulations! You just earned 15 points! Well done!")
#if your color is not recognizable
else:
    print("Color didn't recognize please choose only from red, yellow and green.")

