from typing import Tuple

import gmpy2
from gmpy2 import mpz

from NumThu import gcd_ext
from sympy import Symbol, solve

from StaticEnv import MAX_NUM


def two_unknown_single_eq(x_coff: int, y_coff: int, eq_right: int) -> Tuple:
    """
    求解二元一次方程
    :param x_coff:变量x的系数
    :param y_coff:变量y的系数
    :param eq_right:等式右边的常数项
    :return:通解形式
    """
    gcf, _, _ = gcd_ext(x_coff, y_coff)
    assert eq_right % gcf == 0
    x = Symbol('x')
    y = Symbol('y')
    rel = solve([x_coff*x+y_coff*y-eq_right], [x, y])

    x0 = 0
    y0 = 0
    for i in range(MAX_NUM):
        ret = eval(str(list(rel.values())[0]).replace("y", str(i)))
        if ret % 1 == 0:
            x0 = int(ret)
            y0 = i
            break

    x_gen = f"x = {x0}+{int(y_coff/gcf)}t"
    y_gen = f"y = {y0}-{int(y_coff/gcf)}t"
    return x_gen, y_gen


def single_mod_eq(x_coff: int, eq_right: int, mod: int):
    """
    一次同余方程
    :param x_coff:变量x的系数
    :param eq_right:等式右边的常数项
    :param mod:模数
    :return:通解形式
    """
    gcf, _, _ = gcd_ext(x_coff, mod)
    assert eq_right % gcf == 0, "The Eq. has no solution."
    x0 = 0
    for i in range(mod):
        if (x_coff * i - eq_right) % mod == 0:
            x0 = i
            break
    x_gen = f"x = {x0}+{int(mod / gcf)}t(mod {mod})"
    return x_gen


def single_mod_eqs():
    """
    中国剩余定理求同余方程组
    :return:
    """
    pass


def Legendre(up: int, down: int) -> mpz:
    assert gmpy2.is_odd(down) and gmpy2.is_prime(down)
    return gmpy2.legendre(up, down)


def Jacobi(up: int, down: int) -> mpz:
    assert gmpy2.is_odd(down)
    return gmpy2.jacobi(up, down)


if __name__ == '__main__':
    print(two_unknown_single_eq(2, 3, 7))

    print(single_mod_eq(6, 2, 8))
