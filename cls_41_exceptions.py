# exception = an event that interrupts the flow of a program
#       (zeroDivision, typeError, ValueError)
#       1.try, 2.except, 3.finally

try:
    numb = int(input("Enter a number: "))
    print(1/numb)
except ZeroDivisionError:
    print("you cant't divide by zero idiot!")
except ValueError:
    print("enter only numbers! idiot")
except Exception as e:
    print(f"error: {e}")
finally:
    print("do some clean up here")