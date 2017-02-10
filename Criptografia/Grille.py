#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
import random as r

def def_n(a):
    n=math.sqrt(a)
    if n%2 <> 0:
        n=math.ceil(n)
        if n%2 <> 0:
            n=n+1
    return int(n)

def draw_matrix(m):
    for i in range(len(m)):
        print '[',
        for j in range(len(m[i])):
            print '{:>1s}'.format(str(m[i][j])),
        print ']'

def ini_mat(n,v):
    m=[]
    for i in range(n):
        m.append([v]*n)
    return m

def rotate_90(m,n):
    mat=ini_mat(n,'-')
    l = len(m)
    for i in range(l):
        k=l-1
        for j in range(l):
            mat[k][i]=m[i][j]
            k=k-1
    return mat

def separate(a,block):
    flag=0
    list=[]
    while flag < len(a):
        nc=a[flag:flag+block]
        list.append(nc)
        flag=flag+block
    return list

def ramdon_key(n):
    count=0
    cor=[]
    m=ini_mat(n,'-')
    block=n*n/4

    while count<block:
        s=ini_mat(n,'-')
        flag=True
        rotate=3
        while flag:
            a=r.randint(0, len(m)-1)
            b=r.randint(0, len(m)-1)
            if m[a][b] != '*':
                s[a][b]='*'
                m[a][b]='*'
                #print 'Matriz s:'
                #dibujaMatriz(s)
                cor.append([a,b])
                flag=False
        while rotate !=0:
            s=rotate_90(s,n)
            #print "Matriz s Rotada:"
            #dibujaMatriz(s)
            for i in range(len(m)):
               for j in range(len(m)):
                    if s[i][j] == '*' and m[i][j]!='*':
                        m[i][j]='*'
            #print "esta es m:"
            #dibujaMatriz(m)
            rotate-=1
        count+=1
        #print cor
    return cor

def mat_key(cor,n):
    m=ini_mat(n,'-')
    for i in cor:
        m[i[0]][i[1]]='*'
    draw_matrix(m)
    return m

def cipher(key,text,n):
    m=key
    c=ini_mat(n,'-')
    x=0
    rot=1
    #print text
    while x<len(text):
        for i in range(len(m)):
            for j in range(len(m)):
                if m[i][j] != '-':
                    c[i][j]=text[x]
                    x+=1
        m=rotate_90(m,n)
        print "Rotacion " + str(rot) + ":"
        rot+=1
        draw_matrix(c)

    return c

def decipher(c,key,n):
    d=[]
    rot=1
    while len(d) != n*n:
        for i in range(len(c)):
            for j in range(len(c)):
                if key[i][j] == '*':
                    d.append(c[i][j])
                    c[i][j] = '-'
        key=rotate_90(key,n)
        print "Rotacion " + str(rot) + ":"
        rot+=1
        draw_matrix(c)
        print d
    return d


l=raw_input("Ingrese el mensaje que desea cifrar: "); #Lee Cadena
ori_tam=len(l)
n= def_n(len(l)) #Define el tamaño n de la matriz
text= list(l) #Convierte a l en una lista de caracteres
#print text
tam_mat=n*n #Tamaño de la matriz
if tam_mat > len(l):
    for i in range(len(l),int(tam_mat)):#Completa la cadema si el tamaño
        text.insert(i,'&')              #de la matriz es mayor con el signo $
block= n*n/4 #Define el tamaño del bloque
text = ''.join(text)
text_sep=separate(text,block) #Separa l en bloques
print "Esta es el mensaje de entrada: \"" + l + "\""
print "Este es el mensaje a cifrar completado: \"" + str(text) + "\""
print "La matriz va hacer de tamaño: " + str(n) + "x" + str(n)
print "El tamaño del bloque es: " + str(block)

coor=ramdon_key(n)
coor.sort()
print "Las coordenadas de la llave son: " +  str(coor)
print "La llave sobre la matriz:"
key=mat_key(coor,n)
print "**********CIFRADO*********"
c=cipher(key,text,n)
print "**********DECIFRADO*********"
d=decipher(c,key,n)
d=''.join(d)#Convierte la lista a una cadena
print "El mensaje decifrado es: \"" + str(d[:ori_tam]) + "\""



