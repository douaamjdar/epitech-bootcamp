for i in range(-30, 31):
    if i % 3 == 0:  
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 5 == 0 and i % 3 == 0:
        print("FizzBuzz")
    else:
        print(i)