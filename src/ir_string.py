from __future__ import annotations
from base64 import b64decode, b64encode, b85decode, b85encode
from zlib import compress, decompress


def _enc(n):
    if n < 0 or 0xFFFFFF <= n: raise Exception('out of range')
    return b64encode( n.to_bytes(3, 'big') ).decode()

def _dec(s):
    try:
        return int.from_bytes( b64decode( s.encode() ), 'big' )
    except:
        raise Exception('invalid code')

def _zip(text: str):
    b = compress(text.encode())
    return b85encode(b).decode()

def _unzip(text: str):
    b = b85decode(text)
    return decompress(b).decode()

"""
def encode(data: list[int]):
    return _zip("".join([_enc(n) for n in data]))

def decode(string: str):
    raw = _unzip(string)
    if len(raw) % 4: raise Exception('invalid code')
    return [_dec( raw[x:x+4] ) for x in range(0, len(raw), 4)]
"""

def encode(data: list[int]):
    return _zip(":".join([str(n) for n in data]))

def decode(string: str):
    raw = _unzip(string)
    return [int(x) for x in raw.split(':')]