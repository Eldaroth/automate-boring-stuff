def spam():
    global eggs
    eggs = "spam"


eggs = "global"
spam()

# due to spam() before the print the global eggs variant will be invoked, i.e. "spam"
print(eggs)
