import math

def mcd(num1,num2):
    if num1 > num1:
        a=num1
        b=num2
    else:
        a=num2
        b=num1
    div = divmod(a,b)
    while div[1]!=0:
        a = b
        b = div[1]
        div=divmod(a,b)
    return b

def powmod(a,b,n):
    aux=a**b
    mod=aux%n
    return mod

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

def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    return y

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        return None  # modular inverse does not exist
    else:
        return x % m

#m=raw_input("Ingrese el mensaje a cifrar: ")
m=6882326879666683
#p=raw_input("Ingrese p:  ")
p=47
#q=raw_input("Ingrese q:  ")
q=71
#t=raw_input("Ingrese t:  ")
t=6
n=int(p)*int(q)
fi= (int(p)-1)*(int(q)-1)
ver_e=0
while ver_e !=1:
    e=raw_input("Ingrese e: ")
    ver_e= mcd(fi,int(e))


#print powmod(688,19,3337)


tam_m=len(str(m))
print tam_m
inf=0
sup=int(math.ceil(float(tam_m)/float(t)))
#sup=tam_m/t
#print tam_m
arr=sublist(str(m),sup)
print "**************CIFRADO****************"
c=[]
for i in arr:
    print "Powmod("+str(i)+","+str(e)+","+str(n)+")"
    var1=powmod(int(i),int(e),n)
    print var1
    c.append(str(var1))
print "El mensaje cifrado es: " + str(c)

eea=egcd(fi,int(e))
print "\nEste es el y del EEA: " + str(eea) +"\n"

print "***************DECIFRADO****************"
d=[]
for i in c:
    print "Powmod("+str(i)+","+str(eea)+","+str(n)+")"
    var2=powmod(int(i),int(eea),n)
    print var2
    d.append(str(var2))

print "El mensaje decifrado es: " + str(d)



