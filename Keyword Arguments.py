# Keyword arguments = an argument preceded by an identifier
#                       helps with readability
#                       order of arguments doesnt matter
#                       1. position 2. default 3.KEYWORD 4. arbitrary


# def hello (greeting,title, first,last):
#     print(f"{greeting} {title} {first} {last}")
#
# hello(last="Hello",first="Mr",greeting="Spongebob",title="Squarepants")

# print("1","2","3" , sep="-")

def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"
phone_num = get_phone(country=1, area=123, first=456,last=7890)
print(phone_num)