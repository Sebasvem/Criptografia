import random as r

def rotate_90(m,n):
    mat=ini_mat(n,'-')
    l = len(m)
    for i in range(l):
        k=l-1
        for j in range(l):
            mat[k][i]=m[i][j]
            k=k-1
    return mat

def dibujaMatriz(M):
    for i in range(len(M)):
        print '[',
        for j in range(len(M[i])):
            print '{:>1s}'.format(str(M[i][j])),
        print ']'

def ini_mat(n,v):
    m=[]
    for i in range(n):
        m.append([v]*n)
    return m

def ramdon_key(n):
    count=0
    cor=[]
    m=ini_mat(n,'-')
    block=n*n/4

    while count<block:
        #print 'Iteracion: '+ str(count)
        s=ini_mat(n,'-')
        flag=True
        rotate=3
        while flag:
            #print "holii"
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
        print cor
    return cor

n=6
block=n*n/4
m=ini_mat(n,'-')
ramdon_key(n)
















