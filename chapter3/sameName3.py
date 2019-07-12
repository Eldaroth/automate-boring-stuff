def spam():
    global eggs
    eggs = "spam"  # this is global


def bacon():
    eggs = "bacon"  # this is local


def ham():
    print(eggs)  # this uses the global variable


eggs = 42  # this is global
spam()
print(eggs)
