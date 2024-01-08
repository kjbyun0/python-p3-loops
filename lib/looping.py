#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    i = 10
    while i > 0:
        print(i)
        i -= 1
    print('Happy New Year!')

def square_integers(int_list):
    # code goes here!
    return [num * num for num in int_list]

def fizzbuzz():
    # code goes here!
    for i in range(1, 101):
        mod_3 = i % 3
        mod_5 = i % 5
        if mod_3 == 0 and mod_5 == 0:
            print('FizzBuzz')
        elif mod_3 == 0:
            print('Fizz')
        elif mod_5 == 0:
            print('Buzz')
        else:
            print(i)
