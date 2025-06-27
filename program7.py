n = 17
is_prime = all(n % i != 0 for i in range(2, n))
print(f"{n} is prime? {is_prime}")
