def listInput(list):
    for i in list[:-1]:
        print(i + ", ", end="")
    print("and " + list[-1])


spam = ["apples", "bananas", "tofu", "cats"]
listInput(spam)

transportation = ["car", "motorcycle", "bicycle", "scooter", "rollerskates"]
listInput(transportation)
