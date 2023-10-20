def is_palindrome(number):
    # Convert the number to a string to make it easier to check for palindrome
    num_str = str(number)
    
    # Reverse the string
    reversed_str = num_str[::-1]
    
    # Compare the original string with the reversed string
    if num_str == reversed_str:
        return True
    else:
        return False

# Input a number from the user
num = int(input("Enter a number:"))

if is_palindrome(num):
    print(f"{num} is a palindrome")
else:
    print(f"{num} is not a palindrome")