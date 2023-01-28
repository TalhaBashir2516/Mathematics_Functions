
print("Welcome!")

def Kaprekars_Constant():
    iterations = 0
    def One_Iteration(number):
        ascending = sorted(number)
        descending = sorted(number, reverse=True)
        ascending_number = 1000*int(ascending[0]) + 100*int(ascending[1]) + 10*int(ascending[2]) + int(ascending[3])
        descending_number = 1000*int(descending[0]) + 100*int(descending[1]) + 10*int(descending[2]) + int(descending[3])
        return(str(descending_number - ascending_number))


    number = input('Enter any four digit number: ')
    while number != '6174':
        iterations += 1
        number = One_Iteration(number)
    print(f'Number of iterations are {iterations}')
        


Kaprekars_Constant()


