# logical operator

temp = int(input("\nwhat is the temperature outside?"))

if temp < 0:
    print("invalid temperature")
elif temp > 0 and temp <= 30:
    print("Go out and enjoy the day!")
elif temp >= 31:
    print("It is kinda hot to go outside")
else:
    print("invalid input")

season = int(input("\ninput what season do you like \n1)summer\n2)winter\n choice(1/2): "))

if season == 1:
    print("Okay, I see you like summer!\n")
    is_hot = int(input("What's the hottest temperature you've ever felt? "))
    if is_hot < 0:
        print("that's not summer temperature")
    elif is_hot > 0 and is_hot < 30:
        print("that's normal summer temperature")
    elif is_hot > 30 and is_hot <=90:
        print("that's okay temperature to be in")
    elif is_hot > 90 and is_hot < 100:
        print("that's hot enough")
    elif is_hot == 100 or is_hot > 100:
        print("that's pretty hot")
elif season == 2:
    print("Okay, I see you like winter!\n")
    is_cold = int(input("What's the coldest tempereature you've ever felt? "))
    if is_cold > 0:
        print("Are you sure? that's not cold!")
    elif is_cold < 0 and is_cold >= -5:
        print("that's normal cold temperature!")
    elif is_cold < -5 and is_cold >= -10:
        print("that's cold enough!")
    elif is_cold < -10:
        print("that's quite cold!")