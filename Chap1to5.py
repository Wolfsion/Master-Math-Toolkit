import gmpy2
from gmpy2 import mpz


def gcd_ext(num1: int, num2: int) -> (mpz, mpz, mpz):
    gcf = gmpy2.gcd(num1, num2)
    r, s = gmpy2.gcdext(num1, num2)
    return gcf, r, s


def lowest_common_multiple(num1: int, num2: int) -> mpz:
    multi = abs(num1*num2)
    lcm = multi / gmpy2.gcd(num1, num2)
    return lcm


def inverse(num: int, mod: int) -> mpz:
    ins = gmpy2.invert(num, mod)
    return ins


def is_prime(num: int) -> bool:
    return gmpy2.is_prime(num)


def pow_mod(base: int, index: int, mod: int) -> mpz:
    _ret = gmpy2.powmod(base, index, mod)
    return _ret


if __name__ == '__main__':
    test = lowest_common_multiple(100, 99)
    print(test)

