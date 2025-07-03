#tip=int(input("Enter tip precentage: "))

choice=int(input("""")
select your choice 
1 - 15%
2 - 18%
3 - 20%
4 - type number
"""))

if choice == 1: 
    print("Standard")
elif choice == 2:
    print("good")
elif choice == 3:
    print("great")
elif choice == 4:
   tip=int(input("Enter tip precentage: "))
   if tip > 20:
    print("My hero")
    else:  print("provide right precentage")
else:
    print("provide right precentage")
