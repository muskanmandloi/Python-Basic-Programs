# TRY WITH FINALLY

try:
    i = int(input("enter a number : "))
    c = 1/i 
except Exception as e:
    print(e)
    exit()
finally:
    print("We are done!")