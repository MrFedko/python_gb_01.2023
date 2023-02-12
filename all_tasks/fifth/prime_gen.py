def prime_gen(n: int) -> (iter, int):
    primes_list = []
    current_number = 2
    while len(primes_list) < n:
        is_prime = True
        for num in primes_list:
            if current_number % num == 0:
                is_prime = False
                break
        if is_prime:
            primes_list.append(current_number)
            yield current_number
        current_number += 1
