#!/usr/bin/env python
# -*- coding: latin-1 -*-

def ParHex(hex):
    pHex=[]
    dec=[]
    imp=[]
    for i in range(0,len(hex)-1,2):
        pHex.append(hex[i]+hex[i+1])
    for i in pHex:
        dec.append(int(i, 16))
    for i in dec:
         imp.append(unichr(i))
    imp = "".join(imp)
    return imp

def become_bin(text,l):
    if type(text) is str:
        c=bin(int(text, 16))[2:]
    else:
        c=bin(text)[2:]
    c=list(c)
    tam=len(c)
    while tam < l:
        c.insert(0,'0')
        tam+=1
    return c

def become_hex(text,l):
    if type(text) is str:
        c=hex(int(text, 2))[2:]
    else:
        c=hex(text)[2:-1]
    c=list(c)
    tam=len(c)
    while tam < l:
        c.insert(0,'0')
        tam+=1
    return c

def pc_1(kb,p):
    k56=[]
    for i in p:
        x=kb[i]
        k56.append(x)
    return k56

def Calculate_C(c):
    aux=c[:]
    list_of_C=[]
    for i in range(16):
        c=aux[:]
        for j in range(27):
            if i == 0 or i == 1 or i == 8 or i == 15:
                if j==0:
                    aux[27]= c[0]
                aux[j] = c[j+1]
            else:
                if j==0:
                    aux[27]= c[1]
                if j==26:
                    aux[26]=c[0]
                else:
                    aux[j] = c[j+2]
        list_of_C.append(aux[:])
    return list_of_C

def Calculate_D(d):
    aux=d[:]
    list_of_D=[]
    for i in range(16):
        d=aux[:]
        for j in range(27):
            if i == 0 or i == 1 or i == 8 or i == 15:
                if j==0:
                    aux[27]= d[0]
                aux[j] = d[j+1]
            else:
                if j==0:
                    aux[27]= d[1]
                if j==26:
                    aux[j] = d[0]
                else:
                    aux[j] = d[j+2]
        list_of_D.append(aux[:])
    return list_of_D

def concatenate(c1,d1):
    zero=0
    keys=[]
    while zero < len(c1):
        k=cp[zero] + d1[zero]
        keys.append(k[:])
        zero+=1
    return keys

def pc_2(cd,p):
    key16=[]
    for i in cd:
        keyaux=[]
        ki=i
        for j in p:
            x=ki[j]
            keyaux.append(x)
        key16.append(keyaux[:])
    return key16

def IP(mb,initp):
    mp=[]
    for i in initp:
        x=mb[i]
        mp.append(x)
    return mp

def coor_sbox(dx1,dx2):
    if dx1 == 0:
        snum = (dx1+1)*dx2
    elif (dx1==1):
        snum = (dx1+1)*8+dx2
    elif dx1==2:
        snum = (dx1+2)*8+dx2
    else:
        snum = (dx1+3)*8+dx2
    return snum

def fper(cad,fip):
    fp_1=[]
    for i in fip:
        x=cad[i]
        fp_1.append(x)
    return fp_1

######################### PARTE 2 #############################
def lmi(ml,mr,k):
    #print k
    li=[]
    ri=[]
    li.append(ml[:]) #Agregar L0
    li.append(mr[:]) #Agrega L1
    ri.append(mr[:]) #Agregar R0
    i=0
    while i < 16:
        rix = rmi(li[i],ri[i],k[i])
        ri.append(rix[:])
        li.append(rix[:])
        i+=1
    return ri[16] + li[16]

def rmi(ml,mr,k): #  Se Calcula Ri y se hace todo el proceso para S
    exp = exp_tab(mr,expansion_table)
    xorke = xorE(k,exp)
    sb = s_box(xorke, sbox)
    lxf = lxorf(sb,ml)
    #print lxf
    return lxf

def lxorf(a,b):
    lf=[]
    for i in range(len(a)):
        if a[i]==b[i]:
            lf.append("0")
        else:
            lf.append("1")
    return lf

def exp_tab(r, exptab):
    e=[]
    for i in exptab:
        x=r[i]
        e.append(x)
    return e

def xorE(kcd,e):
    kxor=[]
    kaux=[]
    for j in range(48):
        if j==0:
            kaux=[]
        if kcd[j]==e[j]:
            kaux.append("0")
        else:
            kaux.append("1")
    kxor.append(kaux[:])
    return kxor

def permutation(slist,p):
    mper=[]
    for i in p:
        x=slist[i]
        mper.append(x)
    return mper

def s_box(x,s):
    xo=x[0]
    i=0
    n=6
    si=0
    sres=[]
    while i < 48:
        slist=[]
        aux=[]
        for a in range(i,n):
            aux.append(xo[a])
        x1 = str(aux[0]) + str(aux[5])
        x2 = "".join(aux[1:5])
        dx1 = int(x1,2)
        dx2 = int(x2,2)
        snum=coor_sbox(dx1,dx2)
        stab=s[si]
        sres.append(str(stab[snum]))
        i+=6
        n+=6
        si+=1
    for j in sres:
        entero=int(j)
        s1=become_bin(entero,4)
        s1="".join(s1)
        slist.append(s1[:])
    slist="".join(slist)
    permu=permutation(slist,per)
    return permu

############################# PARTE 2 ########################################
# Permutation and translation tables for DES
pc1 = [56, 48, 40, 32, 24, 16,  8,  0,
       57, 49, 41, 33, 25, 17,  9,  1,
       58, 50, 42, 34, 26, 18, 10,  2,
       59, 51, 43, 35, 62, 54, 46, 38,
       30, 22, 14,  6, 61, 53, 45, 37,
       29, 21, 13,  5, 60, 52, 44, 36,
       28, 20, 12,  4, 27, 19, 11,  3]
# permuted choice key (table 2)
pc2 = [ 13, 16, 10, 23,  0,  4,
         2, 27, 14,  5, 20,  9,
        22, 18, 11,  3, 25,  7,
        15,  6, 26, 19, 12,  1,
        40, 51, 30, 36, 46, 54,
        29, 39, 50, 44, 32, 47,
        43, 48, 38, 55, 33, 52,
        45, 41, 49, 35, 28, 31]

# initial permutation IP
ip = [57, 49, 41, 33, 25, 17, 9,  1,
      59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5,
      63, 55, 47, 39, 31, 23, 15, 7,
      56, 48, 40, 32, 24, 16, 8,  0,
      58, 50, 42, 34, 26, 18, 10, 2,
      60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6]

# Expansion table for turning 32 bit blocks into 48 bits
expansion_table = [
    31,  0,  1,  2,  3,  4,
    3,  4,  5,  6,  7,  8,
    7,  8,  9, 10, 11, 12,
    11, 12, 13, 14, 15, 16,
    15, 16, 17, 18, 19, 20,
    19, 20, 21, 22, 23, 24,
    23, 24, 25, 26, 27, 28,
    27, 28, 29, 30, 31,  0 ]

# The (in)famous S-boxes
sbox = [
   # S1
   [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7,
    0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8,
    4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0,
    15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],

    # S2
    [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10,
     3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5,
     0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15,
     13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],

    # S3
    [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8,
     13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1,
     13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7,
     1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],

    # S4
    [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15,
     13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9,
     10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4,
     3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],

    # S5
    [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9,
     14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6,
     4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14,
     11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],

    # S6
    [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11,
     10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8,
     9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6,
     4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],

    # S7
    [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1,
     13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6,
     1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2,
     6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],

    # S8
    [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7,
     1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2,
     7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8,
     2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],
    ]

# 32-bit permutation function P used on the output of the S-boxes
per = [ 15, 6, 19, 20, 28, 11,
        27, 16, 0, 14, 22, 25,
        4, 17, 30, 9, 1, 7,
        23,13, 31, 26, 2, 8,
        18, 12, 29, 5, 21, 10,
        3, 24]

# final permutation IP^-1
fp = [  39,  7, 47, 15, 55, 23, 63, 31,
        38,  6, 46, 14, 54, 22, 62, 30,
        37,  5, 45, 13, 53, 21, 61, 29,
        36,  4, 44, 12, 52, 20, 60, 28,
        35,  3, 43, 11, 51, 19, 59, 27,
        34,  2, 42, 10, 50, 18, 58, 26,
        33,  1, 41,  9, 49, 17, 57, 25,
        32,  0, 40,  8, 48, 16, 56, 24]

def complete_m(message):
    listm=list(message)
    tam=len(listm)
    while tam % 16 != 0:
        listm.insert(0,'0')
        tam+=1
    listm="".join(listm)
    return listm

def ECB_Mode(ciph):
    ecbm=[]
    for i in ciph:
        down=0
        up=4
        while up < len(i)+1:
            block = i[down:up]
            block=list(block)
            num=block[0]
            for x in range(len(block)-1):
                block[x] = block[x+1]
            block[3]=num
            block="".join(block)
            ecbm.append(block[:])
            down=up
            up+=4
    return ecbm

def ECB_Mode_inv(ciph):
    ecbm=[]
    up=0
    while up < len(ciph):
        block = ciph[up]
        block=list(block)
        num=block[3]
        for x in range(len(block)-1,0,-1):
            block[x] = block[x-1]
        block[0]=num
        block="".join(block)
        ecbm.append(block[:])
        up+=1
    return ecbm

def asciiToHex(m):
    m=list(m)
    c=[]
    for i in m:
        c .append(format(ord(i), "x"))
    #print c
    c="".join(c)
    #print c
    c=list(c)
    return c


############################## PARTE 1 ###############################

k="aaaaaaaa"
#k = "133457799BBCDFF1" #Llave
kHex=asciiToHex(k)

#k = raw_input("Ingrese la llave:")

kbin = become_bin(k,64) #Convierte la llave a binario
kprima = pc_1(kbin,pc1) #Hala k' haciendo pc1(k)
kc = kprima[:28] #Divide k' en los primeros 28 bits
kd = kprima[28:] #Divide k' en los ultimos 28 bits
cp = Calculate_C(kc) # Calcula todos los Ci
dp = Calculate_D(kd) # Calcula todos los Di
contcd = concatenate(cp,dp) #Concatena CiDi
keycd = pc_2(contcd,pc2) #Halla las 16 llaves, haciendo pc2(CiDi)

############################ PARTE 2 ##################################
print "**********************************************CIFRADO*************************************************"
m = "123"
print "Este es la llave en Hexa: \n\t","".join(kHex)
#m = raw_input("Ingrese el mensaje: ")
print "Este es m: \n\t" + "".join((list(m)))
mHex=asciiToHex(m)
print "Este es m convertido a Hex: \n\t" + "".join(mHex)
print "Este es m: \n\t" + ParHex(mHex)
tam_m=len(mHex)
mHex = "".join(mHex)
mbin = become_bin(mHex, len(mHex))
print "Este es mHex convertido a bin: \n\t" + "".join(mbin) + "\t" + str(len(mbin))
mHex=list(mHex)
mc=complete_m(mHex)
print "Este es mHex completado a 64: \n\t" + "".join(mc)
tam_mc = len(mc)
mbin64 = become_bin(mc, len(mc)*4)
print "Este es mHex64 convertido a bin: \n\t" + "".join(mbin64)
tam_mbin=len(mbin64)
tam_div = tam_mbin/64
print "Este es el numero de iteraciones de DES: \n\t" + str(tam_div)
iLower = 0
iUpper = 64
cipher=[]

print "Estos son los " +str(tam_div)+ " bloques cifrados:"

while(tam_div > 0):
    mbinprim=mbin64[iLower : iUpper]
    mprima = IP(mbinprim,ip)
    ml = mprima[:32] #Divide m' en los primeros 32 bits
    mr = mprima[32:] #Divide m' en los ultimos 32 bits
    prueba = lmi(ml,mr,keycd)
    cip= fper(prueba,fp)
    cip = "".join(cip)
    cipher.append(cip[:])
    iLower =iUpper
    iUpper+=64
    print "\tBloque " + str((tam_div%-4)*-1) + " :" +str(cip)
    tam_div-=1


if len(cipher) > 1:
    ecb = ECB_Mode(cipher)
    print "Aqui se aplico ECB: \n\t" +str("".join(ecb))
    #ecb="".join(ecb)
    #print ecb #Mensaje cifrado concatenado
#hexcip = hex(int(cipher,2))[2:-1]
#print hexcip






#################################Decifrado####################################

print "\n**********************************************DECIFRADO*************************************************"
if len(cipher)>1:
    ecb_inv=ECB_Mode_inv(ecb)
    ecb_inv="".join(ecb_inv)
    print "Aqui se aplica ECB^-1: \n\t" + ecb_inv
    cipher[0] = ecb_inv[:64]
    cipher[1] = ecb_inv[64:]
tam_cip=len(cipher)
ind=0
decipherBin=""
decipherHex=""
while tam_cip > 0:
    cipherIP=IP(cipher[ind],ip);
    cl = cipherIP[:32] #Dividide a cipherIP en sus primeros 32 bits
    cr = cipherIP[32:] #Dividide a cipherIP en sus ultimos 32 bits
    keycdinver=keycd[::-1] # Invierte los elementos del arreglo de las llaves
    de_prueba= lmi(cl,cr,keycdinver) # Obteniene L0 y R0
    dec_mprima = de_prueba[:32]+de_prueba[32:]
    decip=fper(dec_mprima,fp)
    qZero=(tam_mc-tam_m)*4
    if tam_cip == len(cipher):
        decip = "".join(decip[qZero+2:])
    else:
        decip = "".join(decip)
    decipherBin=decipherBin+decip
    #print decip
    hexcip = become_hex(decipherBin,len(decipherBin)/4)
    hexcip = "".join(hexcip)
    #decipherHex=decipherHex+hexcip
    #print hexcip
    ind+=1
    tam_cip-=1

print "Este es el descifrado en binario: \n\t" + decipherBin , len(decipherBin)
print "Este es el descifrado en Hexa: " + hexcip

hexcip= ParHex(hexcip)
print "Este es el mensaje original: " + hexcip


