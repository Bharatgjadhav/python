menu ="""
 0. chose 0 to quit
 1. chose 1 to add
 2. chose 2 to sub
 3. chose 3 to multi
 4. chose 4 to div

"""
chose= None


while(chose != 0):
    print(menu)
    num1 =int(input('first num is: '))
    num2 =int(input('second num is: '))
    chose= int(input("plz enter your chose: "))
    if(chose == 1):

        print(num1, " + ",num2," = ",num1+num2)
    elif(chose == 2):
        print(num1, " - ",num2," = ",num1+num2)
    elif(chose == 3):
        print(num1, " * ",num2," = ",num1+num2)
    elif(chose == 4):
        if(num2 == 0):
            print("You can not divide by zero")
        else:
            print(num1, " / ",num2," = ",num1+num2)
    else:
        print('plz enter a correct option')