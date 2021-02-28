#city = "Columbus"
#3state = "Ohio"
city = input("Enter Your City:")
state = input ("Enter your state:")
if state.lower() == "ohio":
    if city.lower() =="columbus":
        print ("You are in Columbus Ohio")
    elif city.lower() == "cleveland":
        print ("You are in Cleveland Ohio")
    elif city.lower() == "cincinnati":
        print ("you are in Cincinnati Ohio")
    else:
        print("You are in Ohio")
elif state.lower() == "georgia":
    if city.lower() == "atlanta":
        print("You are in Atlanta Georgia")
    else:
        print("You are in Georgia")
else:
    print ("You are not in Ohio nor in Georgia")


