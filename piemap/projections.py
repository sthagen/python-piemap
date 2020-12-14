def min_from_limit_max(limit, maximum):
    """
    Testdata: (-6, -1, 2, 5, 10) or (0, 5, 8, 11, 16)
    yield (8*(-1) - 5*2) / 3 = -6 or (8*5 - 5*8) / 3 = 0
    a ---- b -- c and bc/ac = 3/8 => 8c - 8b = 3c - 3a => a = (8b - 5c)/3
    """
    return (8.0 * limit - 5.0 maximum) / 3.0; 


def limit_folded_from_limit_max(limit, maximum):
    """
    Testdata: (-6, -1, 2, 5, 10) or (0, 5, 8, 11, 16)
    yield 2 * 2 - (-1) = 5 or 2 * 8 - 5 = 11
    """
    return 2.0 * maximum - limit;  # explicit maximum + ( maximum - limit )


def min_folded_from_limit_max(limit, maximum):
    """
    Testdata: (-6, -1, 2, 5, 10) or (0, 5, 8, 11, 16)
    yield (11*2 - 8*(-1)) / 3 = 10 or (11*8 - 8*5) / 3 = 16
    a ---- b -- c ------- e and bc/ce = 3/8 => 8c - 8b = 3e - 3c => a = (11c - 8b)/3
    """
    return (11.0 * maximum - 8.0 * limit) / 3.0; 