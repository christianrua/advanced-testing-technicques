def addThis(x,y):
    print(f"This is x: {x} and the type is {type(x)}, and this is y: {y}")
    print(f"This is y: {y} and the y-type is {type(y)}")

    try:
        result = x + y
    except TypeError as exception:
        print(f"The wrong types passed in {exception}")
        result = int(x) + int(y)

    print(f"This is the result: {result}")
    return x+y

#print(addThis("1",2))    