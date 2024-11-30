def mobilephone():
    mobile=input("Enter the number")
    if mobile[0] == "7" or "8" or "9":
        if len(mobile) == 10:
            print(mobile +" " "is valid");
        else:
            print(mobile +" " "is not valid")


mobilephone()
