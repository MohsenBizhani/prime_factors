def get_prime_factors(number):
    factors = list()
    divisor = 2
    while (divisor <= number):
        if (number % divisor) == 0:
            factors.append(divisor)
            number /= divisor
        else:
            divisor += 1
    return factors


if __name__ == '__main__':
    n = int(input("Enter a number: "))
    print(f"prime factors of {n}: {get_prime_factors(n)}")
