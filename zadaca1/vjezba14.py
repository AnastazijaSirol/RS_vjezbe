#1
def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print(isPrime(2))
print(isPrime(6))

#2
def primes_in_range(start, end):
    return [broj for broj in range(start, end + 1) if isPrime(broj)]

print(primes_in_range(1, 10))
