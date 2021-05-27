""" even_number=[]
given_number=[1,22,33,667,5,31,3,2,10,33]

for number in given_number:
    if number %2==0:
        even_number.append(number)

print(even_number) """
given_number=[1,22,33,667,5,31,3,2,10,33]
even_numbers=[number for number in given_number if number % 2 ==0]
print(even_numbers)