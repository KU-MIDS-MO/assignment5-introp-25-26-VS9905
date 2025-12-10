def approx_real_root(coeffs, interval):

    #cubic polynomial f(x)
    def poly(x):
        c0, c1, c2, c3 = coeffs
        return c0 + c1 * x + c2 * x ** 2 + c3 * x ** 3

    #derivative f'(x)
    def dpoly(x):
        _, c1, c2, c3 = coeffs
        return c1 + c2 * x ** 2 + c3 * x ** 3

    a, b = interval
    x = (a + b) / 2                   #midpoint

    for _ in range(1000):
        fx = poly(x)
        dfx = dpoly(x)

        if dfx == 0:
            break

        new = x - fx / dfx

        if abs(new - x) < 1e-9:
            return new
        x = new

    return x
