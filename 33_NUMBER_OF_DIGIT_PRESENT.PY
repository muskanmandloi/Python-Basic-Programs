# PYTHON PROGRAM TO COUNT THE NUMBER OF DIGITS PRESENT  IN A NUMBER

num=3214
count = 0
while num!=0:
    num //= 10
    count += 1
print("number of digits:" +str(count))