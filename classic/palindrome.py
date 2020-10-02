# Comparing 2 strings to check if it's a Palindrome
string = input("Enter a string: ")
reversedString = ''.join(reversed(string))

if string == reversedString:
    print("It's a Palindrome!")
else:
    print("It's not a Palindrome")

# Or, by address
reversedString = reversed(string)

if list(string) == list(reversedString):
    print("It's a Palindrome!")
else:
    print("It's not a Palindrome")
