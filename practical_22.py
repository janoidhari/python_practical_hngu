# 22.Write a Python program for Error Handling.

print(" ")
try:
    a = int(input("Enter First Number: "))
    b = 0
    c = a / b
    print("Division is : ", c)
except:
    print("Can't divide with zero")
finally:
    print("Rest of the code..")
