from numbers import Integral


def my_range(start: int, end: int, step: float = 1):
    step_is_integer = bool(int(step))

    if step_is_integer:
        _range = range(start, end, step)
        return list(_range)

    _range = [
        start,
    ]
    while _range[-1] <= end:
        next_value = _range[-1] + step
        _range.append(next_value)

    return _range[:-1]


def my_range_fixed(start: int, end: int, step: float = 1):
    """creates a new range implementation with non-integer step"""
    if isinstance(step, Integral):
        _range = range(start, end, step)
        return list(_range)

    _range = [
        start,
    ]
    while _range[-1] <= end - step:
        next_value = _range[-1] + step
        _range.append(next_value)

    return _range


range1 = my_range(0, 1, 0.11)
breakpoint()
range2 = my_range(0, 10)
range3 = my_range(10, 15, 1.5)
