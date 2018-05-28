name = input("Please enter your name: ")
age = int(input("Enter your age: "))
if 18 <= age < 31:
# if age <= 18 or age > 31:
    print("Welcome to holiday, {}".format(name))
else:
    print("Kindly, fuck off {}".format(name))
