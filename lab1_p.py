name = input("Enter your name, please\n")
print("Hello, " + name)
age = int(input("Enter your age, please\n"))
if age < 18:
    print("This user is minor, because his/her age is " + str(age))
else:
    print("This user is adult, because his/her age is " + str(age))

# calculation
a = 10
b = 3
c = 4
print(str(a) + 'x' + '+' + str(b) + 'y' + '+' + str(c) + '=' + '0')
D = b*b - 4*a*c
print('Discriminant -> ' + str(D))