tweet = input()
try:

    if len(str(tweet)) > 42:
        raise ("Error")
except:

    print("Error")
else:
    print("Posted")