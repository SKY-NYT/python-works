# Membership operators = used to test whether a value or variable is found in a sequence
#                        (string, list tuples set and dictionary )
#                        1. in
#                        2. not in

# word = "APPLE"
#
# letter = input("Guess a letter in the secret word: ")
# if letter not in word:
#     print(f"{letter} was not found")
# else:
#     print(f"There is a {letter} ")

email = "BroCode@gmail.com"

if "@" in email and "."in email:
    print("Valid email")
else:
    print("Invalid email")