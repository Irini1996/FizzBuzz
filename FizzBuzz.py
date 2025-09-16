for i in range(1, 101):
    is_multiple_of_3 = i % 3 == 0
    is_multiple_of_5 = i % 5 == 0

    if is_multiple_of_3 and is_multiple_of_5:
        print("FizzBuzz")
    elif is_multiple_of_3:
        print("Fizz")
    elif is_multiple_of_5:
        print("Buzz")
    else:
        print(i)