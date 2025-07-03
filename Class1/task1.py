age =int(input("Enter your age: "))

if age > 0 and age < 13:
    print("child")
elif age >=18 and age < 65:
    print("adult")
elif age >=65:
    print("Elder")
else:
    print("Provide right age")
