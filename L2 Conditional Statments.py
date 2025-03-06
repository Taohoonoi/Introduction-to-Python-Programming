# condintal statments
# if, elif, else

# if condition:
if (5 > 2):
    print("5 is greater than 2")
# elif condition:
elif (5 < 2):
    print("5 is less than 2")
# else:
else:
    print("5 is equal to 2")

# it is used to replace the multiple if else statments 
# match case is also known as switch case in other programming languages

x: str = "Patrick"
match x:
    case "Patrick":
        x = "Pat"
    case "Nittiwat":
        x = "Nort"
    case "Johnny":
        x = "John"
    case _:
        print("invalid number")