#Basic calculator program
class Calcls:
    print("select operation")
    print("1.ADD")
    print("2.SUBTRACT")
    print("3.MULTIPLY")
    print("4.DIVIDE")
    while True:
        choice=input("Enter Choice: ")
        if choice in ('1','2','3','4'):
            num1 = float(input("Enter number: "))
            num2 = float(input("Enter number: "))
            if choice == '1':
                print (num1 + num2)
            elif choice == '2':
                print(num1 - num2)
            elif choice == '3':
                print(num1 * num2)
            elif choice == '4':
                print(num1 / num2)
            break
        else:
            print("Invalid Input")
