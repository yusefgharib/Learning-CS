num, prime = int(input()), False
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            prime = False
            break
        else:
            prime = True
if prime:
    print("This number is prime")
else: 
    print("This number is not prime")
