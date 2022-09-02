def solution(m,f):
    m = int(m)
    f = int(f)
    gen = 0
    while True:
        if m < f:
            result = int(f / m)
            if f % m == 0:
                result -= 1
            f -= result * m
            gen += result
        elif m > f:
            result = int(m / f)
            if m % f == 0:
                result -=1
            m -= result * f
            gen += result
        elif m == 1 and f == 1:
            return str(gen)
        else:
            return "impossible"
