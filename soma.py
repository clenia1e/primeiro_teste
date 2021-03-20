first_number = int(input("type the first value \n"))
second_number = int(input("type the second value \n"))
option = int(input(" 1- to sum \n 2 - to subtract \n"))
if(option == 1):
    calc = first_number + second_number
else:
    calc = first_number - second_number
print(f"the value is: {calc}")