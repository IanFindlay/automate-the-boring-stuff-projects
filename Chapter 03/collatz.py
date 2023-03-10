###Collatz Sequence###

def collatz(number):
    if number == 1:
       print("You can't escape the Collatz infite loop!")
    elif number % 2 == 0:
        print(number/2)
        collatz(number/2)
    else:
        print(number*3 + 1)
        collatz(number*3 + 1)


