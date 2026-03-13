num1 = int(input("son1: "))
num2 = int(input("son2: "))
amal = input("amal: ")

if amal == "+":
    print(num1 + num2)
elif amal == "*":
    print(num1 * num2)
elif amal == "-":
    print(num1 - num2)
elif amal == "/":
    if num2 == 0:
        print("Nolga bolinmaydi")
    else:
        print(num1 / num2)
