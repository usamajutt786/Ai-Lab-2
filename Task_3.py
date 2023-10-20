
def addition(a,b):
    return a+b
def substract(a,b):
    return a-b
def divide(a,b):
    return a/b
def multipy(a,b):
    return a*b
def ShowMenu():
    print("1.Add")
    print("2.Subtract ")
    print("3.Divide")
    print("4.Multiply")

num1=int(input("Enter First number: "))
num2=int(input("Enter Second number: "))
ShowMenu()
choice=int(input("Please Enter Your choice: "))
if choice==1:
    print(addition(num1,num2))
elif choice==2:
    print(substract(num1,num2))
elif choice==3:
    print(float(divide(num1,num2)))
elif choice==4:
    print(multipy(num1,num2))
else:
    print("Invalid Choice....")
    

