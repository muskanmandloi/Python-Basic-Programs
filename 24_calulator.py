# Q30.  PYTHON PROGRAM TO MAKE SIMPLE CALCULATOR

def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y

print("select operations: ")
print("1.ADD")
print("2.SUBTRACT")
print("3.MULTIPLY")
print("4.DIVIDE")

while True:
    choice=input("enter choices(1/2/3/4):")
    if choice in ('1','2','3','4'):
        num1=float(input("enter 1st number: "))
        num2=float(input("enter 2nd number: "))

        if choice == '1':
            print(num1,"+",num2,"=",add(num1,num2))
        elif choice == '2':
             print(num1,"-",num2,"=",subtract(num1,num2))
        elif choice =='3':
             print(num1,"*",num2,"=",multiply(num1,num2))
        elif choice == '4':
             print(num1,"/",num2,"=",divide(num1,num2))
             break
        else:
            print("invalid input")





