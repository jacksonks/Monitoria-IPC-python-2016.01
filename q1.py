n=int(input("tamanho das listas:"))
l1=[]
l2=[]
l3=[]

for i in range(n):
    a=int(input("l1:"))
    l1.append(a)
    b=int(input("l2:"))
    l2.append(b)

for i in range(n): #erro: for i in range(l1):
    l3.append(l1[i])
    l3.append(l2[i]) 
    
print(l1)
print(l2)
print(l3)