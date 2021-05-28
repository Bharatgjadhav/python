number1 = 10
number2 = 20
numbers = [[2,3],2,3,4]
def changeNumber(number1, number2):
    number1 = 30
    number2 = 40
    print('in function changeNumber, number1 = ',number1,'number2= ',number2)
def changeNumbers(numbers):
    numbers[1] = 222
    changeNumber(number1,number2)
    print('Outside function changeNumber, number1 = ',number1,'number2 = ',number2)
changeNumbers(numbers)
print('After executing changeNumbers ',numbers)