## Maybe

https://github.com/DavidBuchanan314/rc4
https://github.com/manojpandey/rc4


keyText = '1234567890'
In [135]: f[Dot11WEP].iv + binascii.unhexlify(keyText)
Out[135]: b'=\xdb\xc7\x124Vx\x90'

seed = '=\xdb\xc7\x124Vx\x90'
key = seed

S, j, out = list(range(256)), 0, []
for i in range(256):
    j = (j + S[i] + ord(key[i % len(key)])) % 256
    print('DONE')
    S[i], S[j] = S[j], S[i]
