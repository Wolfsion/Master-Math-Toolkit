from typing import List

import gmpy2
from gmpy2 import mpz


# 求解最大公因数和系数r、s
from StaticEnv import MAX_NUM


def gcd_ext(num1: int, num2: int) -> (mpz, mpz, mpz):
    gcf = gmpy2.gcd(num1, num2)
    rs = gmpy2.gcdext(num1, num2)
    return gcf, rs[0], rs[1]


# 求解最小公倍数
def lowest_common_multiple(num1: int, num2: int) -> mpz:
    lcm = gmpy2.lcm(num1, num2)
    return lcm


# 求解模逆
def inverse(num: int, mod: int) -> mpz:
    ins = gmpy2.invert(num, mod)
    return ins


# 素性检测
def is_prime(num: int) -> bool:
    return gmpy2.is_prime(num)


# 模幂运算
def pow_mod(base: int, index: int, mod: int) -> mpz:
    _ret = gmpy2.powmod(base, index, mod)
    return _ret


# 欧拉函数
def euler_func(num: int) -> int:
    ret = 1
    for i in range(2, num):
        gcf, _, _ = gcd_ext(i, num)
        if gcf == 1:
            ret += 1
    return ret


# 求阶数
def ord_func(num: int, mod: int) -> int:
    order = 1
    gcf, _, _ = gcd_ext(num, mod)
    assert gcf == 1
    while order <= MAX_NUM and pow_mod(num, order, mod) != 1:
        order += 1
    return order


# 求原根
def primary_root(mod: int) -> List[int]:
    roots = []
    eul = euler_func(mod)
    for i in range(mod):
        gcf, _, _ = gcd_ext(i, mod)
        if gcf == 1:
            order = ord_func(i, mod)
            if order == eul:
                roots.append(i)
    return roots


if __name__ == '__main__':
    test = pow_mod(3, 462, 253)
    print(test)

