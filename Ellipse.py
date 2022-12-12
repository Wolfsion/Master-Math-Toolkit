from fractions import Fraction
from typing import Tuple

from NumThu import inverse


def add_ell_not_char2or3(a4: int, a6: int,
                         x1: int, y1: int, x2: int, y2: int,
                         mod: int = None) -> Tuple[Fraction, Fraction]:
    """
    y^2 = x^3 + a4*x + a6
    :param mod: 如果是有限整数域需指定
    :param a4:
    :param a6:
    :param x1:
    :param y1:
    :param x2:
    :param y2:
    :return:
    """
    delta = -16*(4*a4**3 + 27*a6**3)
    assert delta != 0
    if mod is None:
        if x1 == x2 and y1 == y2:
            eq_lambda = Fraction((3 * x1 ** 2 + a4), (2 * y1))
        else:
            eq_lambda = Fraction((y2 - y1), (x2 - x1))

        x3 = eq_lambda ** 2 - x1 - x2
        y3 = eq_lambda * (x1 - x3) - y1
    else:
        if x1 == x2 and y1 == y2:
            eq_lambda = ((3 * x1 ** 2 + a4) * inverse(2 * y1, mod)) % mod
        else:
            eq_lambda = ((y2 - y1) * inverse(x2 - x1, mod)) % mod
        x3 = (eq_lambda ** 2 - x1 - x2) % mod
        y3 = (eq_lambda * (x1 - x3) - y1) % mod
    return x3, y3


def k_mult_ell_not_char2or3(a4: int, a6: int,
                            x: int, y: int, k: int,
                            mod: int = None) -> Tuple[Fraction, Fraction]:
    """
    y^2 = x^3 + a4*x + a6
    :param mod: 如果是有限整数域需指定
    :param a4:
    :param a6:
    :param x:
    :param y:
    :param k:
    :return:
    """
    xn = x
    yn = y
    for times in range(k - 1):
        xn, yn = add_ell_not_char2or3(a4, a6, xn, yn, x, y, mod)
    return xn, yn


def k_mult_ell_not_char2or3_optim(a4: int, a6: int,
                                  x: int, y: int, k: int,
                                  mod: int = None) -> Tuple[Fraction, Fraction]:
    """
    y^2 = x^3 + a4*x + a6
    :param mod: 如果是有限整数域需指定
    :param a4:
    :param a6:
    :param x:
    :param y:
    :param k:
    :return:
    """
    xn = x
    yn = y
    a_pre_x = x
    a_pre_y = y
    first = True
    k_bin = bin(k).replace('0b', '')[::-1]
    for ind, ch in enumerate(k_bin):
        if ch == '1':
            if first:
                first = False
            else:
                a_pre_x, a_pre_y = add_ell_not_char2or3(a4, a6, a_pre_x, a_pre_y, xn, yn, mod)
        xn, yn = k_mult_ell_not_char2or3(a4, a6, xn, yn, 2, mod)
        print(f"n{ind}={ch}---a{ind}=({a_pre_x}, {a_pre_y}),b{ind+1}=({xn},{yn}).")

    return a_pre_x, a_pre_y


def add_ell_char2(a2: int, a6: int,
                  x1: int, y1: int, x2: int, y2: int) -> Tuple[Fraction, Fraction]:
    """
    y^2 + xy = x^3 + a2*x^2 + a6
    :param a2:
    :param a6:
    :param x1:
    :param y1:
    :param x2:
    :param y2:
    :return:
    """
    if x1 == x2 and y1 == y2:
        eq_lambda = Fraction((x1**2+y1), x1)
    else:
        eq_lambda = Fraction((y2+y1), (x2+x1))

    x3 = eq_lambda**2+eq_lambda+x1+x2+a2
    y3 = eq_lambda*(x1+x3)+x3+y1
    return x3, y3


def k_mult_ell_char2(a4: int, a6: int,
                     x: int, y: int, k: int):
    """
    y^2 + xy = x^3 + a2*x^2 + a6
    :param a4:
    :param a6:
    :param x:
    :param y:
    :param k:
    :return:
    """
    xn = x
    yn = y
    for times in range(k - 1):
        xn, yn = add_ell_char2(a4, a6, xn, yn, x, y)
    return xn, yn


if __name__ == '__main__':
    # print(add_ell_not_char2or3(3, 1, 0, 1, 0, 1))

    # print(k_mult_ell_not_char2or3(3, 1, 0, 1, 5))

    # print(k_mult_ell_not_char2or3_optim(3, 1, 5, 16, 6, mod=23))

    print(k_mult_ell_not_char2or3_optim(3, 7, 1, 27, 79, mod=359))


