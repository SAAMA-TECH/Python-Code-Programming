print("Sayyed Affan Ahmed - 251P088")
try:
    a = int(input('Enter a number: '))
    b = 10 / a
    print(b)
except ZeroDivisionError:
    print('Division by zero error')
except ValuError:
    print('Invalid input')
