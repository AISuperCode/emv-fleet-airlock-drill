"""Small stats helpers (drill repo)."""


def mean(values):
    if not values:
        raise ValueError("mean() arg is an empty sequence")
    return sum(values) / len(values)


def median(values):
    """Return the median of a non-empty sequence of numbers."""
    if not values:
        raise ValueError("median() arg is an empty sequence")
    ordered = sorted(values)
    n = len(ordered)
    mid = n // 2
    if n % 2 == 1:
        # PLANTED BUG (intentional): off-by-one for odd-length input;
        # the first production codetask must add tests and fix this.
        return ordered[mid - 1]
    return (ordered[mid - 1] + ordered[mid]) / 2
