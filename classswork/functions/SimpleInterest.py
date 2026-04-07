#function for calculating simple interest
def calculateSI(p,r,t):
    return((p*r*t)/100)
#taking input
principal = float(input("enter principal"))
rate = float(input("enter rate "))
time = float(input("enter time in years"))
#displaying result
print("Simple Interest on amount",principal,"at rate",rate,"%","in",time,"years is",calculateSI(principal,rate,time))
