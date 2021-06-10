3 # PROGRAM TO CHECK IF A STRING IS PALINDROME OR NOT

my_str='gssjhdauay'
my_str=my_str.casefold()
rev_str=reversed(my_str)
if list(my_str) == list(rev_str):
   print("the string is palindrome")
else:
    print("the string is not palindrome")
