num =int(input("please enter a value range to stop:"))

for i in range (1,num+1):
    if i%3 ==0:
        print ("Fizz", end= " ")
    elif i%5 ==0:
        print ("Buzz", end= " ")
    elif i%15 ==0:
        print ("FizzBuzz", end= " ")
    else:
        print(i, end= " ")