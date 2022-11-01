foc = int(input("Enter the factorial number:"))
factorial = 1
if foc <=0:
    print("No factorial value for zero")
else:
    for i in range(1,foc+1):
        factorial=factorial*i
        print("value for the ",foc,"is",factorial)
