#!/usr/bin/env python
# -*- coding: latin-1 -*-
import copy

def asciiToHex(m):
    m=list(m)
    c=[]
    for i in m:
        c .append(format(ord(i), "x"))
    c="".join(c)
    c=list(c)
    return c

def ini_mat(n,v):
    m=[]
    for i in range(n):
        m.append([v]*n)
    return m

def logicXor(s,r):
    l12=[]
    for i in range(len(s)):
        if s[i]==r[i]:
            l12.append("0")
        else:
            l12.append("1")
    return l12

def div_mkHex(hex):
    pHex=[]
    for i in range(0,len(hex)-1,2):
        pHex.append(hex[i]+hex[i+1])
    return pHex

def sublist(m,n):
    tam_m=len(m)
    var=[]
    iUpper=n
    iLower=0
    while tam_m > 0:
        var.append(m[iLower:iUpper])
        iLower=iUpper
        iUpper+=n
        tam_m-=n
    return var

def draw_matrix(m):
    for i in range(len(m)):
        print '[',
        for j in range(len(m[i])):
            print '{:>1s}'.format(str(m[i][j])),
        print ']'

def rotWord(w):
    lastR=copy.deepcopy(w)
    lastR=lastR[3]
    p0=lastR[0]
    for i in range(0,len(lastR)-1):
        lastR[i]=lastR[i+1]
    lastR[3]=p0
    return lastR

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

def subWord(rot,s_box):
    sb=[]
    for i in rot:
        a=int(i[0],16) # convierte hexa a entero
        b=int(i[1],16)
        sb.append(s_box[a][b])
    return sb

def rcon_bin(rcn):
    rcbin=[]
    for i in rcn:
        rcbin.append(become_bin(i,len(i)*4))
    return rcbin

def rowsToColums(m):
    mrot=ini_mat(len(m),'-')
    for i in range(len(m)):
        for j in range(len(m)):
            mrot[i][j]=m[j][i]
    return mrot

def foundKey(sw,wk,index):
    waux0=[]
    waux=[]
    tam_sw=len(sw)*2
    ind=0
    inde=0

    while tam_sw > 0:
        swbin=become_bin(sw,len(sw)*4)
        swbin=sublist(swbin,8)
        rbin= rcon_bin(rcon)
        rbin_div8=sublist(rbin[index],8)
        #if tam_sw > 12 :
            #print rbin_div8[inde]
        #print str(swbin[inde]) + str(sw)
        #print"----------------------------------------"
        if tam_sw > 12 :
            x12=logicXor(swbin[inde],rbin_div8[inde])
        else:
            x12=swbin[inde]
        xd=wk[ind]
        xd="".join(xd)
        xdbin=become_bin(xd,len(xd)*4)
        xdbin=sublist(xdbin,8)
        #if tam_sw > 12 :
            #print x12
        #print str(xdbin[inde]) + str(wi[ind])
        x34=logicXor(x12,xdbin[inde])
        x34=sublist(x34,4)
        #print x34
        x0= hex(int("".join(x34[0]), 2))[2:]
        y0= hex(int("".join(x34[1]), 2))[2:]
        waux0.append(x0+y0)
        #print x0 , y0, waux0
        inde+=1
        if inde == 4:
            #print "!!!"
            inde=0
            ind+=1
            waux.append(waux0[:])
            sw= "".join(waux0)
            waux0=[]
        #print
        tam_sw-=1
    return waux

def addRoundKey(m,key,ind):
    resaux=[]
    res=[]
    k=key[ind]
    for i in range(len(m)):
        if i > 0:
            res.append(resaux[:])
            resaux=[]
        for j in range(len(m)):
            mbin=become_bin(m[i][j],len(m[i][j])*4)
            kbin=become_bin(k[i][j],len(k[i][j])*4)
            mXork= logicXor(mbin,kbin)
            mXork=sublist(mXork,4)
            x1= hex(int("".join(mXork[0]), 2))[2:]
            y1= hex(int("".join(mXork[1]), 2))[2:]
            resaux.append(x1+y1)
            if i == 3 and j==3:
                res.append(resaux[:])
    return res

def subBytes(rot,s_box):
    sb=[]
    for i in range(len(rot)):
        for j in range(len(rot)):
            hex=rot[i][j]
            a=int(hex[0],16) # convierte hexa a entero
            b=int(hex[1],16)
            sb.append(s_box[a][b])
    sb=sublist(sb,4)
    return sb

def subBytes_Inv(rot,s_box):
    sb=[]
    for i in range(len(rot)):
        for j in range(len(rot)):
            hex=rot[i][j]
            a=int(hex[0],16) # convierte hexa a entero
            b=int(hex[1],16)
            sb.append(s_box[a][b])
    sb=sublist(sb,4)
    return sb

def shiftRow(sb):
    aux=ini_mat(4,'-')
    sbcopy=copy.deepcopy(sb)
    aux_ind=sbcopy[1][0]#e2
    aux_ind1=sbcopy[2][0]#5a
    aux_ind2=sbcopy[2][1]#89
    aux_ind3=sbcopy[3][3]#53
    for i in range(len(sbcopy)):
        for j in range(len(sbcopy)):
            if i == 0 :
                aux[i][j]=sbcopy[i][j]
            if i==1 and j==0 or i==1 and j==1 or i==1 and j==2:
                aux[i][j]=sbcopy[i][j+1]
            elif i==1 and j==3:
                aux[i][j]=aux_ind
            if i==2 and j==0 or i==2 and j==1:
                aux[i][j]=sbcopy[i][j+2]
            elif i==2 and j==2:
                aux[i][j]=aux_ind1
            elif i==2 and j==3:
                aux[i][j]=aux_ind2
            if i==3 and j==1 or i==3 and j==2 or i==3 and j==3:
                aux[i][j]=sbcopy[i][j-1]
            elif i==3 and j==0:
                aux[i][j]=aux_ind3
    return aux

def shiftRowInv(sb):
    aux=ini_mat(4,'-')
    sbcopy=copy.deepcopy(sb)
    aux_ind=sbcopy[1][3]#e2[1][0]
    aux_ind1=sbcopy[2][0]#5a
    aux_ind2=sbcopy[2][1]#89
    aux_ind3=sbcopy[3][0]#dc
    for i in range(len(sbcopy)):
        for j in range(len(sbcopy)):
            if i == 0 :
                aux[i][j]=sbcopy[i][j]

            #if i==1 and j==0 or i==1 and j==1 or i==1 and j==2:
            if i==1 and j==1 or i==1 and j==2 or i==1 and j==3:
                aux[i][j]=sbcopy[i][j-1]
            elif i==1 and j==0:
                aux[i][j]=aux_ind
            if i==2 and j==0 or i==2 and j==1:
                aux[i][j]=sbcopy[i][j+2]
            elif i==2 and j==2:
                aux[i][j]=aux_ind1
            elif i==2 and j==3:
                aux[i][j]=aux_ind2
            if i==3 and j==0 or i==3 and j==1 or i==3 and j==2:
                aux[i][j]=sbcopy[i][j+1]
            elif i==3 and j==3:
                aux[i][j]=aux_ind3
    return aux

def rowMultColum(mix,sr,lt,et):
    arr=[]
    arrbin=[]
    mc_row=[]
    for i in range(len(mix)):
        for j in range(len(mix)):
            s=sr[j]
            m=mix[i][j]
            a0=int(s[0],16)
            a1=int(s[1],16)
            b0=int(m[0],16)
            b1=int(m[1],16)
            if a0==0 and a1==0 or b0==0 and b1==0:
                arr.append("0")
            else:
                a=lt[a0][a1]
                b=lt[b0][b1]
                a=format(int(a,16),'d')
                b=format(int(b,16),'d')
                #print "Deci: ",a,b
                sum=int(a)+int(b)
                #print "suma: ", sum
                mod=sum%255
                mod="".join(hex(mod).split('x')[1])
                if len(mod)==1:
                    mod="0"+str(mod)
                #print "modu: ", mod[0],mod[1]
                e0=int(mod[0],16)
                e1=int(mod[1],16)
                #print e0, e1
                res=et[e0][e1]
                arr.append(res)
    for i in arr:
        arrbin.append(become_bin(i,8))
    arrbin=sublist(arrbin,4)
    for i in arrbin:
        mixor0=logicXor(i[0],i[1])
        mixor1=logicXor(i[2],i[3])
        mixor2=logicXor(mixor0,mixor1)
        mixor2= "".join(mixor2)
        mixor2=hex(int(mixor2, 2))[2:]
        if len(mixor2)==1:
            mixor2="0"+mixor2
        mc_row.append(mixor2)
    #print mc_row
    return mc_row

def mixColum(sr):
        mc=[]
        tam_sr=len(sr)
        ind=0
        while tam_sr > 0:
            var= rowMultColum(mix_mat,sr[ind],l_Table, e_table)
            mc.append(var[:])
            ind+=1
            tam_sr-=1
        return mc
def mixColum_Inv(sr):
        mc=[]
        tam_sr=len(sr)
        ind=0
        while tam_sr > 0:
            var= rowMultColum(mix_inv,sr[ind],l_Table, e_table)
            mc.append(var[:])
            ind+=1
            tam_sr-=1
        return mc

def complete_m(message):
    listm=list(message)
    tam=len(listm)
    while tam % 32 != 0:
        listm.insert(0,'0')
        tam+=1
    listm="".join(listm)
    return listm

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
sbox=[['63','7c','77','7b','f2','6b','6f','c5','30','01','67','2b','fe','d7','ab','76'],
      ['ca','82','c9','7d','fa','59','47','f0','ad','d4','a2','af','9c','a4','72','c0'],
      ['b7','fd','93','26','36','3f','f7','cc','34','a5','e5','f1','71','d8','31','15'],
      ['04','c7','23','c3','18','96','05','9a','07','12','80','e2','eb','27','b2','75'],
      ['09','83','2c','1a','1b','6e','5a','a0','52','3b','d6','b3','29','e3','2f','84'],
      ['53','d1','00','ed','20','fc','b1','5b','6a','cb','be','39','4a','4c','58','cf'],
      ['d0','ef','aa','fb','43','4d','33','85','45','f9','02','7f','50','3c','9f','a8'],
      ['51','a3','40','8f','92','9d','38','f5','bc','b6','da','21','10','ff','f3','d2'],
      ['cd','0c','13','ec','5f','97','44','17','c4','a7','7e','3d','64','5d','19','73'],
      ['60','81','4f','dc','22','2a','90','88','46','ee','b8','14','de','5e','0b','db'],
      ['e0','32','3a','0a','49','06','24','5c','c2','d3','ac','62','91','95','e4','79'],
      ['e7','c8','37','6d','8d','d5','4e','a9','6c','56','f4','ea','65','7a','ae','08'],
      ['ba','78','25','2e','1c','a6','b4','c6','e8','dd','74','1f','4b','bd','8b','8a'],
      ['70','3e','b5','66','48','03','f6','0e','61','35','57','b9','86','c1','1d','9e'],
      ['e1','f8','98','11','69','d9','8e','94','9b','1e','87','e9','ce','55','28','df'],
      ['8c','a1','89','0d','bf','e6','42','68','41','99','2d','0f','b0','54','bb','16']]

sbox_inv=[["52","09","6a","d5","30","36","a5","38","bf","40","a3","9e","81","f3","d7","fb"],
          ["7c","e3","39","82","9b","2f","ff","87","34","8e","43","44","c4","de","e9","cb"],
          ["54","7b","94","32","a6","c2","23","3d","ee","4c","95","0b","42","fa","c3","4e"],
          ["08","2e","a1","66","28","d9","24","b2","76","5b","a2","49","6d","8b","d1","25"],
          ["72","f8","f6","64","86","68","98","16","d4","a4","5c","cc","5d","65","b6","92"],
          ["6c","70","48","50","fd","ed","b9","da","5e","15","46","57","a7","8d","9d","84"],
          ["90","d8","ab","00","8c","bc","d3","0a","f7","e4","58","05","b8","b3","45","06"],
          ["d0","2c","1e","8f","ca","3f","0f","02","c1","af","bd","03","01","13","8a","6b"],
          ["3a","91","11","41","4f","67","dc","ea","97","f2","cf","ce","f0","b4","e6","73"],
          ["96","ac","74","22","e7","ad","35","85","e2","f9","37","e8","1c","75","df","6e"],
          ["47","f1","1a","71","1d","29","c5","89","6f","b7","62","0e","aa","18","be","1b"],
          ["fc","56","3e","4b","c6","d2","79","20","9a","db","c0","fe","78","cd","5a","f4"],
          ["1f","dd","a8","33","88","07","c7","31","b1","12","10","59","27","80","ec","5f"],
          ["60","51","7f","a9","19","b5","4a","0d","2d","e5","7a","9f","93","c9","9c","ef"],
          ["a0","e0","3b","4d","ae","2a","f5","b0","c8","eb","bb","3c","83","53","99","61"],
          ["17","2b","04","7e","ba","77","d6","26","e1","69","14","63","55","21","0c","7d"]]

rcon=[ "01000000", "02000000", "04000000", "08000000", "10000000", "20000000", "40000000", "80000000", "1b000000","36000000"]

mix_mat=[["02","03","01","01"],
         ["01","02","03","01"],
         ["01","01","02","03"],
         ["03","01","01","02"]]

mix_inv=[["0e","0b","0d","09"],
         ["09","0e","0b","0d"],
         ["0d","09","0e","0b"],
         ["0b","0d","09","0e"]]

l_Table=[["00","00","19","01","32","02","1a","c6","4b","c7","1b","68","33","ee","df","03"],
         ["64","04","e0","0e","34","8d","81","ef","4c","71","08","c8","f8","69","1c","c1"],
         ["7d","c2","1d","b5","f9","b9","27","6a","4d","e4","a6","72","9a","c9","09","78"],
         ["65","2f","8a","05","21","0f","e1","24","12","f0","82","45","35","93","da","8e"],
         ["96","8f","db","bd","36","d0","ce","94","13","5c","d2","f1","40","46","83","38"],
         ["66","dd","fd","30","bf","06","8b","62","b3","25","e2","98","22","88","91","10"],
         ["7e","6e","48","c3","a3","b6","1e","42","3a","6b","28","54","fa","85","3d","ba"],
         ["2b","79","0a","15","9b","9f","5e","ca","4e","d4","ac","e5","f3","73","a7","57"],
         ["af","58","a8","50","f4","ea","d6","74","4f","ae","e9","d5","e7","e6","ad","e8"],
         ["2c","d7","75","7a","eb","16","0b","f5","59","cb","5f","b0","9c","a9","51","a0"],
         ["7f","0c","f6","6f","17","c4","49","ec","d8","43","1f","2d","a4","76","7b","b7"],
         ["cc","bb","3e","5a","fb","60","b1","86","3b","52","a1","6c","aa","55","29","9d"],
         ["97","b2","87","90","61","be","dc","fc","bc","95","cf","cd","37","3f","5b","d1"],
         ["53","39","84","3c","41","a2","6d","47","14","2a","9e","5d","56","f2","d3","ab"],
         ["44","11","92","d9","23","20","2e","89","b4","7c","b8","26","77","99","e3","a5"],
         ["67","4a","ed","de","c5","31","fe","18","0d","63","8c","80","c0","f7","70","07"],]

e_table=[["01","03","05","0f","11","33","55","ff","1a","2e","72","96","a1","f8","13","35"],
         ["5f","e1","38","48","d8","73","95","a4","f7","02","06","0a","1e","22","66","aa"],
         ["e5","34","5c","e4","37","59","eb","26","6a","be","d9","70","90","ab","e6","31"],
         ["53","f5","04","0c","14","3c","44","cc","4f","d1","68","b8","d3","6e","b2","cd"],
         ["4c","d4","67","a9","e0","3b","4d","d7","62","a6","f1","08","18","28","78","88"],
         ["83","9e","b9","d0","6b","bd","dc","7f","81","98","b3","ce","49","db","76","9a"],
         ["b5","c4","57","f9","10","30","50","f0","0b","1d","27","69","bb","d6","61","a3"],
         ["fe","19","2b","7d","87","92","ad","ec","2f","71","93","ae","e9","20","60","a0"],
         ["fb","16","3a","4e","d2","6d","b7","c2","5d","e7","32","56","fa","15","3f","41"],
         ["c3","5e","e2","3d","47","c9","40","c0","5b","ed","2c","74","9c","bf","da","75"],
         ["9f","ba","d5","64","ac","ef","2a","7e","82","9d","bc","df","7a","8e","89","80"],
         ["9b","b6","c1","58","e8","23","65","af","ea","25","6f","b1","c8","43","c5","54"],
         ["fc","1f","21","63","a5","f4","07","09","1b","2d","77","99","b0","cb","46","ca"],
         ["45","cf","4a","de","79","8b","86","91","a8","e3","3e","42","c6","51","f3","0e"],
         ["12","36","5a","ee","29","7b","8d","8c","8f","8a","85","94","a7","f2","0d","17"],
         ["39","4b","dd","7c","84","97","a2","fd","1c","24","6c","b4","c7","52","f6","01"]]

#########################KEY GENERATION######################
keys=[]
w=[]

k="2b7e151628aed2a6abf7158809cf4f3c"
k=div_mkHex(k)
k=sublist(k,4)
wi=k[:]
w.append(wi[:])
k=rowsToColums(k)
keys.append(k)
rounds=10
w_ind=0
while rounds > 0:
    r=rotWord(w[w_ind])
    sw=subWord(r,sbox)
    sw="".join(sw)
    wau=foundKey(sw,w[w_ind],w_ind)
    w.append(wau[:])
    keys.append(rowsToColums(wau))
    #draw_matrix(keys)
    w_ind+=1
    rounds-=1
##################CIFRADO#####################
#m=raw_input(Ingrese el mensaje a cifrar: )
print"**********************************CIFRADO********************************"
m="Hóy füi a camelöt"
print "Mensaje original: ", m
mHex=asciiToHex(m)
print "Mensaje en Hexa: ", "".join(mHex)
mHex="".join(mHex)
tam_mHex=len(mHex)
mc=complete_m(mHex)
tam_mc=len(mc)
print "Mensaje completado: ",  mc
#m="414553206573206d757920666163696c"
tam_div=tam_mc/32
print "Numero de iteraciones de AES: ", tam_div
iLower = 0
iUpper = 32
cipher=[]
while tam_div > 0:
    m=mc[iLower:iUpper]

    m=div_mkHex(m)
    m=sublist(m,4)
    m=rowsToColums(m)
    #draw_matrix(m)
    rounds_mc=10
    ind_mc=0
    while rounds_mc>0:
        if ind_mc > 0:
            m=mc_mat[:]

        #draw_matrix(m)
        ark=addRoundKey(m,keys,ind_mc)
        #draw_matrix(ark)
        sb_ark=subBytes(ark,sbox)
        sr=shiftRow(sb_ark)
        #draw_matrix(sr)
        #print
        sr_rot=rowsToColums(sr)
        mc_mat=mixColum(sr_rot)
        mc_mat=rowsToColums(mc_mat)
        #draw_matrix(mc_mat)
        #print
        ind_mc+=1
        rounds_mc-=1
    output=addRoundKey(sr,keys,10)
    #print output
    cipher.append(output[:])
    iLower=iUpper
    iUpper+=32
    tam_div-=1
listcip=[]
for i in cipher:
    print "Bloque 1: \n", draw_matrix(i),"\n"
for i in range(len(cipher)):
    for j in range(len(cipher)*2):
        listcip.append("".join(cipher[i][j]))
listcip="".join(listcip)
print "Este es el mensaje cifrado: ", listcip

############################DECIFRADO###################################
print"************************************DECIFRADO*****************************************"
keys_inv=keys[::-1]
tam_cip=len(cipher)
indcip=0
decipher=[]
while tam_cip > 0:
    rounds_mc_inv=10
    ind_mc_inv=0
    output=cipher[indcip]
    while rounds_mc_inv>0:
        if ind_mc_inv > 0:
            output=sb_srInv[:]
        arkInv=addRoundKey(output,keys_inv,ind_mc_inv)
        if ind_mc_inv == 0:
            srInv=shiftRowInv(arkInv)
        else:
            arkInv=rowsToColums(arkInv)
            mcInv=mixColum_Inv(arkInv)
            mcInv=rowsToColums(mcInv)
            srInv=shiftRowInv(mcInv)
        sb_srInv=subBytes_Inv(srInv,sbox_inv)
        ind_mc_inv+=1
        rounds_mc_inv-=1
    decip=addRoundKey(sb_srInv,keys_inv,10)
    decip = rowsToColums(decip)
    decipher.append(decip[:])
    print "Matriz descifrada: "
    draw_matrix(decip)
    indcip+=1
    tam_cip-=1
print decipher
listdec=[]
for i in range(len(decipher)):
    for j in range(len(decipher)*2): #Cambiar entre 2 y 4
        listdec.append("".join(decipher[i][j]))
print listdec
listdec="".join(listdec)
print listdec
qZero=(tam_mc-tam_mHex)
print listdec[qZero:]
decipher = ParHex(listdec)
print "Mensaje Original Decifrado: ", decipher
