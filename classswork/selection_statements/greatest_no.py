a = int(input("enter first number"))
b = int(input("enter second number"))
c = int(input("enter third number"))
d = int(input("enter fourth number"))
e = int(input("enter fifth number"))

if (a >= b and a >= c and a >= d and a >= e): 
    print(a," is greatest among all")
elif( b >= a and b >= c and b >= d and b >= e):
    print(b,"is greatest among all numbers")
elif( c >= a and c >= b and c >= d and c >= e):
    print(c,"is greatest among all numbers")
elif(d >= a and d >= b and d >= c and d >= e):          
    print(d,"is greatest among all numbers")
else:
    print(e,"is greatest among all numbers")

  
