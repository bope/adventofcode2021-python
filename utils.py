from time import perf_counter


def time(f, *args, **kwargs):
    s = perf_counter()
    r = f(*args, **kwargs)
    t = perf_counter() - s
    return r, t
