import time

print("PYCAL VERSION 3.09.04")
print("COPYRIGHT VOID STUDIOS 2025-2026")
print("\n Welcome to The Py Calculator.")
# The intro


while True:
    print("\nAddition [+], Multiplication [x], Division [/], Subtraction [-], Power [^], Remainder [*], Percentage of [%], Percent of [>].")
    calculator = input("\n [Input] ")
    # Allows the input

    if calculator.lower() == "exit":
        print("\n The EXIT Command has been activated. There is no cancelation of the Command")
        print("\n FIVE SECONDS")
        time.sleep(1); print("\n4 SECONDS LEFT.")
        time.sleep(1); print("3 SECONDS LEFT.")
        time.sleep(1); print("2 SECONDS LEFT.")
        time.sleep(1); print("PROGRAM END.")
        time.sleep(0.5); break
        

    if calculator == "+":
        a = float(input("\n Enter first number: "))
        b = float(input("\n Enter second number: "))
        total = a + b
        print("\n Here is your total: "), print(total)


    elif calculator == "x":
        c = float(input("\n Enter first number: "))
        d = float(input("\n Enter second number: "))
        total = c * d
        print("\n Here is your total: "), print(total)


    elif calculator == "/":
        e = float(input("\n Enter first number: "))
        f = float(input("\n Enter second number: "))
        total = e / f
        print("\n Here is your total: "), print(total)


    elif calculator == "-":
        g = float(input("\n Enter first number: "))
        h = float(input("\n Enter second number: "))
        total = g - h
        print("\n Here is your total: "), print(total)


    elif calculator == "^":
        base = float(input("\n Enter the base number: "))
        exponent = float(input("Enter the exponent: "))
        total = base ** exponent
        print("\n Here is your total: "), print(total)


    elif calculator == "*":
        i = float(input("\n Enter first number: "))
        j = float(input("\n Enter second number: "))
        total = i % j
        print("\n Here is your total: "), print(total)


    elif calculator == "%":
        percent = float(input("\n Enter percent: "))
        num = float(input("Enter number: "))
        total = (percent / 100) * num
        print("\n Here is your total: "), print(total)


    elif calculator == ">":
        num = float(input("Enter part number: "))
        total = float(input("Enter total number: "))
        percent = (num / total) * 100
        print(f"\n {num} is {percent}% of {total}")


    elif calculator == "Log":
        print("\n Log: 1.02.03; Added the Log, to log updates for users. | 1.03.03; Added Division capability. | 1.04.03; Added Subtraction capability. | 1.05.03; Added Power capability. | 1.06.03; Added Remainder capability. | 1.06.04; Added developer notes within the code. | 1.07.04; Added Percentage capabilities. | 1.08.04; Added Perfentage Of capabilities | 2.08.04; changed the operation names from letters to symbols for easier usage of the program | 3.08.04: Remade it to allow loops and easier of use | 3.09.04: Changed input handling")


    if calculator not in ["+", "x", "/", "-", "^", "*", "%", ">", "Log"]:
        print("\n INVALID.")

#use this to find words:   
#!!SEARCH-FUNCTION DOES NOT WORK IN TERMINAL
