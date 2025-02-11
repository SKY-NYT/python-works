# function = A block of reusable code
#  place () after the function name to invoke it

def song (name,age):
    print(f"Happy birthday to {name}!")
    print(f"You are  {age} years old!")
    print(f"Happy birthday to {name}!")

song("kofi",22)

# return = statement used to end a function and
# send a result back to the caller

def add(x, y):
    z = x + y
    return z

def substract(x, y):
    z = x - y
    return z

def multiply(x, y):
    z = x * y
    return z

def divide(x, y):
    z = x / y
    return z

print(add(45, 6))
print(substract(21, 12))
print(multiply(3, 4))
print(divide(9,3))

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("Kofi", "Frimpong")

print(full_name)