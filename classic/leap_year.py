year = int(input("Enter a year: "))

# First stat: checks if is a century leap year
# Second stat: checks if the first is true or false
# Third stat: checks if a non-century year is leap 
if ((year % 400 == 0) if (year % 100 == 0) else (year % 4 == 0)):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")

