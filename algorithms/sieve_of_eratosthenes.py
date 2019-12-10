# From CTCI.
# Vijayarajan Govindarajan 2018

def get_prime_numbers_upto(number):
    sieve = []
    sieve.insert(0,False)
    sieve.insert(1,False)
    for i in range(2, number):
        sieve.insert(i,True)

    prime = 2

    while (prime < len(sieve)):
        sieve = remove_non_primes(prime, sieve)
        prime = get_next_prime(prime, sieve)
        print(prime)

    return sieve


def remove_non_primes(prime, sieve):
    for i in range(prime*prime, len(sieve), prime):
        #print(prime, i)
        sieve[i] = False
    #print(sieve)
    return sieve

def get_next_prime(prime, sieve):
    next_prime = prime + 1
    while (len(sieve) > next_prime and (not sieve[next_prime])):
        next_prime = next_prime + 1
    return next_prime



def main():
    sieve = get_prime_numbers_upto(10000000)
    #print(sieve)
    for i in range(2,len(sieve)):
        if sieve[i]:
            print(i)

if __name__ == "__main__":
    main()