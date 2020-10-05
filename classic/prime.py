def is_prime(num):
    prime = True
    if num < 2:
        prime = False
    else:
        for i in range(2, num // 2):
            if (num % i) == 0:
                prime = False
                break
    if prime:
        print("Number {} is prime" .format(num))
    else:
        print("Number {} is not a prime number" .format(num))

is_prime(int(input("Enter a number: ")))