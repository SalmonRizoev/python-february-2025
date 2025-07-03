years=int(input("Enter number of years: "))
choice=input("""
select your choice:
1 - Days
2 - weeks
3 - hours
""")

if choice == "1":
    print(f"In {years} years there are {365*years}days")
elif choice == "2":
    print(f"In {years} years there are {52*years} weeks")
else:
    print("select a right choice")




