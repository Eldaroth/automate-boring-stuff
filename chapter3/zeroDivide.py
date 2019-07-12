def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print("Error: Invalid argument.")


print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))


def spam2(divideBy):
    return 42 / divideBy


# code below will stop by spam2(0), because once the code jumps
# to the except clause, it does not return to the try clause
print()
try:
    print(spam2(2))
    print(spam2(12))
    print(spam2(0))
    print(spam2(1))
except ZeroDivisionError:
    print("Error: Invalid argument.")
