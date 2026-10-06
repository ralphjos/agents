from decimal import Decimal, getcontext


def calculate_pi_like_series(terms: int) -> Decimal:
    getcontext().prec = 50
    total = Decimal(0)
    sign = 1

    for n in range(terms):
        denominator = 2 * n + 1
        term = Decimal(sign) / Decimal(denominator)
        total += term
        sign *= -1

    return total * 4


if __name__ == "__main__":
    terms = 1_000_000
    result = calculate_pi_like_series(terms)
    print(f"{result}")
