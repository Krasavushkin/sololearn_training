try:
    name = input()
    if len(str(name)) <= 3:
        raise ("Invalid Name")
except:
    print("Invalid Name")

else:
    print("Account Created")