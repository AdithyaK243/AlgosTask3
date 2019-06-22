def minimumSum(num):
    # to create a list of prime numbers till num
    primes = []
    for possiblePrime in range(2, num):
        isPrime = True
        for i in range(2, possiblePrime):
            if possiblePrime % i == 0:
                isPrime = False

        if isPrime:
            primes.append(possiblePrime)

    # creates a list of the numbers
    numArray = []
    for i in range(1, num):
        numArray.append(i+1)

    total = 0
    for prime in primes:
        primeIndex = primes.index(prime)
        for number in numArray:
            numIndex = numArray.index(number)
            if number % prime == 0:
                numArray.pop(numIndex)

        total += primeIndex + 1

    return total


def main():
    num = int(input(""))
    print(minimumSum(num))


if __name__ == "__main__":
    main()
