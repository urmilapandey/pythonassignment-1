#Given an integer x, return true if x is a palindrome, and false otherwise. (LeetCode: Palindrome 
#Number) 

x = int(input("Enter an integer: "))
str_x = str(x)ss
if str_x == str_x[::-1]:
   print(f"{x} is a palindrome.")
else:
    print(f"{x} is not a palindrome.")

