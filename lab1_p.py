name = input("Enter your name, please\n")
print("Hello, " + name)
age = int(input("Enter your age, please\n"))
if age < 18:
    print("This user is minor, because his/her age is " + str(age))
else:
    print("This user is adult, because his/her age is " + str(age))