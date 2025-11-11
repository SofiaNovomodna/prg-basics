def f(n):
    primes = []
    i = 2  # start checking from 2 (the first prime)

    while len(primes) < n:  # keep finding primes until we have n of them
        is_prime = True
        for ii in range(2, i -1):
            if i % ii == 0:
                is_prime = False
                break

        if is_prime:
            primes.append(i)

        i += 1  # check the next number

    return primes[n - 1]  # lists are 0-indexed


if __name__ == "__main__":
    print(f(1))  # → 2
    print(f(5))  # → 11
