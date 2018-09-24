def hano(n,a,b,c):
    if n==1:
        print(a,"-->",c)
    else:
        hano(n-1,a,c,b)
        print(a,"-->",c)
        hano(n-1,b,a,c)

a="塔1"
b="塔2"
c="塔3"
hano(3,a,b,c)