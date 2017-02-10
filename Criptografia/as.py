#!/usr/bin/env python
# -*- coding: latin-1 -*-
# -*- coding: 850 -*-
import binascii
m="Höy me füi a cåmelôt"
#m="Hoy me fui a camelot"
print len(m)
m=list(m)
c=[]
for i in m:
    c .append(format(ord(i), "x"))
print c
print len(c)

dec=[]
for i in c:
    dec.append(int(i, 16))
print dec
print len(dec)
for i in dec:
    print unichr(i)