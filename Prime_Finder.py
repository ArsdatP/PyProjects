def prime_finder(n):

    #list to host prime numbers
    primes = []

    for i in range(2, n+1):
        for x in range(2, n+1):
            if i % x == 1 and i not in primes:
                primes.append(i)
            else:
                break
    return primes


print(prime_finder(23))
