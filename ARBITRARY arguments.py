# *args         = allows you to pass multiple non-key arguments
# **kwargs       = allows you to pass multiple keyword-arguments
#                 * unpacking operator
#                 1. position 2. default 3.keyword 4. ARBITRARY


def shipping_label(*args,**kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    # for value in kwargs.values():
    #     print(value, end=" ")
    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    elif "pobox" in kwargs:
        print(f"{kwargs.get('street')}")
        print(f"{kwargs.get('pobox')}")
    else:
        print(f"{kwargs.get('city')}" )
    print(f"{kwargs.get('city')} {kwargs.get('state')}, {kwargs.get('zip')}")

shipping_label("Dr", "spongebob", "Squarepants", "III",
              street="123 Fake street",
               pobox="PO Box #1001",
              city="Detroit",
              state="MI",
              zip="54321")