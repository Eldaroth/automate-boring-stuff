import re

# more complex variant
def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != "-":
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != "-":
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True


# phoneNumber = "415-555-4242"
# print(phoneNumber + " is a phone number:")
# print(isPhoneNumber(phoneNumber))
# noPhoneNumber = "Moshi moshi"
# print(noPhoneNumber + " is a phone number:")
# print(isPhoneNumber(noPhoneNumber))

message = "Call me at 415-555-1011 tomorrow. 415-555-9999 is my office."
for i in range(len(message)):
    chunk = message[i : i + 12]
    if isPhoneNumber(chunk):
        print("Phone number found: " + chunk)
print("Done with a function\n")

# Variant with regular expressions (no function required)
phone_num_regex = re.compile(r"\d{3}-\d{3}-\d{4}")
match = phone_num_regex.findall(message)
for number in match:
    print("Phone number found: " + number)
print("Done with regular expressions\n")
