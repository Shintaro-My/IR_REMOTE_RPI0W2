from __future__ import annotations

def _fmt(n):
    if n < 0 or 0xFFFF <= n: raise Exception('out of range')
    return "%0.4X" % n

def encode(data: list[int]):
    return "".join([_fmt(n) for n in data])

def decode(string: str):
    if len(string) % 4: raise Exception('invalid code')
    return [int(string[x:x+3], 16) for x in range(0, len(string), 3)]