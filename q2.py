def f (n):
    i=1 #erro: i=0
    lista=[]
    while (i <= n): #erro: while (i < n):
        if (n%i == 0):
            lista.append(i)
            i+=1
        else:
            i+=1
    return lista #erro: *esqueci de colocar o 'return lista'

n=333
print(f(n))