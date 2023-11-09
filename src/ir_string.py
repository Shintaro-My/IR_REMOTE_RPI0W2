from __future__ import annotations
from base64 import b64decode as bdec, b64encode as benc


"""
def _enc(n):
    if n < 0 or int('F' * DIGIT, 16) <= n: raise Exception('out of range')
    return benc( n.to_bytes(3, 'big') ).decode()

def _dec(s):
    try:
        return int.from_bytes( bdec( s.encode() ), 'big' )
    except:
        raise Exception('invalid code')

def encode(data: list[int]):
    return "".join([_enc(n) for n in data])

def decode(string: str):
    if len(string) % 4: raise Exception('invalid code')
    return [_dec( string[x:x+4] ) for x in range(0, len(string), 4)]
"""


def _enc(n):
    if n < 0: raise Exception('out of range')
    return benc( n.to_bytes((n.bit_length() + 7) // 8, 'big') ).decode()

def _dec(s):
    try:
        return int.from_bytes( bdec( s.encode() ), 'big' )
    except:
        raise Exception('invalid code')

def encode(data: list[int]):
    return ":".join([_enc(n) for n in data])

def decode(string: str):
    return [_dec( s ) for s in string.split(':')]