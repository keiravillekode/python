import functools

@functools.lru_cache(maxsize=None)
def moves(poles, discs):
    if discs <= 1:
        return discs

    assert poles >= 3

    if poles == 3:
        return 2 ** discs - 1

    return min([2 * moves(poles, d) + moves(poles - 1, discs - d) for d in range(1, discs)])
