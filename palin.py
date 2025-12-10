import sys

if len(sys.argv) > 1:
    string = sys.argv[1]
else:
    string = input("Enter a string: ")

# Check palindrome (case-insensitive)
if string.lower() == string[::-1].lower():
    print(f"'{string}' is a palindrome.")
else:
    print(f"'{string}' is not a palindrome.")
