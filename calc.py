"""Drill target: a tiny arithmetic module for the codetask airlock rehearsal."""


def add(a: int, b: int) -> int:
    # PLANTED BUG (intentional): subtracts instead of adding.
    return a - b


def sub(a: int, b: int) -> int:
    return a - b
