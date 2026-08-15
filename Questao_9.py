n1 = int(input("Digite um numero: "))
n2 = int(input("Digite um numero: "))

if n1>n2:
    n1,n2=n2,n1

while n1<n2-1:
    n1+=1
    print(n1)
