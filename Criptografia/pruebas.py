def asciiToHex(m):
    m=list(m)
    c=[]
    for i in m:
        #c.append(hex(ord(i)))
        c .append(format(ord(i), "x"))
    #print c
    #c="".join(c)
    #print c
    c=list(c)
    return c

m='aaaaaaaa'
hex=asciiToHex(m)
print hex