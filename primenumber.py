#python program to print all the prime numbers in a given range.

#A prime number is a number whose factors are 1 and itself.

low = int(input("Enter the lower part of the range: "))
high = int(input("Enter the upper part of the range: "))

for number in range(low, high + 1):
    if number > 1: 
        for i in range(2, number):
            if number % i == 0:
                break
        else: 
            print(number)
