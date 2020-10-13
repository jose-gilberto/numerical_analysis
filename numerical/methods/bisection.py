
def bisection(a, b, TOL, n0, f, log=False):
    # Step 1
    i = 1
    FA = f(a)
    # Step 2
    while i <= n0:
        # Step 3
        p = a + (b - a)/2
        FP = f(p)
        # Step 4
        if (FP == 0) or ((b - a)/2 < TOL):
            return p
        # Step 5
        i = i + 1
        # Step 6
        if FA * FP > 0:
            a = p
            FA = FP
        else:
            b = p  # FA não muda
    # Step 7
    raise OverflowError(
        'Method failed after N0 iterations, N0 = {}'.format(n0))


if __name__ == "__main__":

    def func(x):
        return x**3 + 4*x**2 - 10

    ans = bisection(1, 2, 0.005, 100, func)
    print(ans)
