


print("                Claculator App By Darshan 😎")
print("")
while True:

    print("1. Addition +")
    print("2. Subtraction -")
    print("3. Multiplication x")
    print("4. Division /")
    print("5. Exit The App")
    print("")
    try:
        a = int(input("Enter Your Choice : "))
        if a >= 6:
            print("BRO Choose From The Menu Only (1 To 5) 🛑🛑")
        print("")

        if a == 1:
            try:
                b = int(input("Enter Your 1st Number : "))
                c = int(input("Enter Your 2nd Number : "))
                print(f"Answer = {b+c} ✅")
                print("")
            except ValueError:
                print("Enter Number Only And Don't Enter Without Filling The Number 😐")
                print("")

        elif a == 2:
            try:
                b = int(input("Enter Your 1st Number : "))
                c = int(input("Enter Your 2nd Number : "))
                print("")
                print(f"Answer = {b-c} ✅")
                print("")
            except ValueError:
                print("Enter Number Only And Don't Enter Without Filling The Number Plzzzzz 😐")
                print("")

        elif a == 3:
            try:
                b = int(input("Enter Your 1st Number : "))
                c = int(input("Enter Your 2nd Number : "))
                print("")
                print(f"Answer = {b*c} ✅")
                print("")
            except ValueError:
                print("BROUU! Enter Number Only And Don't Enter Without Filling The Number 😐")
                print("")

        elif a == 4:
            try:    
                b = int(input("Enter Your 1st Number : "))
                c = int(input("Enter Your 2nd Number : "))
                print("")
                if c == 0:
                    print("Cannot Divide By Zero ❌")
                else:
                    print(f"Answer = {b/c} ✅")
                    print("")
            except ValueError:
                print("SIRRR! Enter Number Only And Don't Enter Without Filling The Number 😭😭")
                print("")

        elif a == 5:
          print("App Closed Byeeee! 😁👋🏻")
          print("")
          break 
    
    except ValueError:
        print("Choose From The Menu Only (1 To 5) 🛑")
        print("")