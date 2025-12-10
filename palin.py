def is_palindrome(value):
    # Convert everything to string safely
    s = str(value).lower()
    return s == s[::-1]

# Fixed test value or replace with your own
value = "Malayalam"

if is_palindrome(value):
    print(f"'{value}' is a palindrome")
else:
    print(f"'{value}' is not a palindrome")
