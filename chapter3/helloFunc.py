def hello():
    print("Howdy!")
    print("Howdy!!!")
    print("Hello there.")


def hello2(name):
    print("Hello " + name)


# There is not really a function overloading in Python like in Java,
# instead you can define one of the parameters as "optional" with =None
def superHello(name=None):
    if name is None:
        print("Howdy!")
        print("Howdy!!!")
        print("Hello there.")
    else:
        print("Hello " + name)


hello()
hello2("Flavio")
superHello()
superHello("Flavio")
