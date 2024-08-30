def maior_3(a,b,c):
    if a>=b and a>=c:
        return a
    elif b>=c:
        return b
    else:
        return c

n1 = int(input('digite uma numero'))
n2 = int(input('digite uma numero'))
n3 = int(input('digite uma numero'))
resultado = maior_3(n1,n2,n3)
print(resultado)