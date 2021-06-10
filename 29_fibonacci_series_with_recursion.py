# PYTHON PROGRAM TO DISPLAY THE FIBONACCI SERIES BY RECURSION 

def recu_fun(n): 
    if n<=1: 
        return n
    else:
        return(recu_fun(n-1)+recu_fun(n-2))
nterms = 10 
if nterms <= 0:
    print("please enter positive integer : ")
else:
    print("fibonacci series : ")
    for i in range(nterms):
        print(recu_fun(i))