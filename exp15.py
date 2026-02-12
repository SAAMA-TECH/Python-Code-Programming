'''AIM: Demonstrate the use of a Python debugger (e.g., pdb or an IDE with debugging
capabilities) on a sample program with intentional errors. Guide students on setting
breakpoints, stepping through code, and examining variable values'''
print("SAYYED AFFAN AHMED")
def calculate_average(numbers):
    total = 0
    for i in range(len(numbers)):
        total = total + numbers[i]
    avg = total / len(numbers)   
    return avg

marks = [10, 20, 30, 40]
result = calculate_average(marks)
print("Average =", result)
