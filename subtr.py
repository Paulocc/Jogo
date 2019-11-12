n1=int(input("Digite um numero: "))
n2=int(input("Digite um numéro: "))
resul = n1-n2
i=0
num=2
while i<resul:
    div=2
    nprimo=0
    while num>div:
        if num%div==0:
            nprimo+=1
            break
        else:
            div+=1
    if nprimo==0:
        if resul-i==1:
            print(num)
        else:
            print(num,end=", ")
        num+=1
        i+=1
    else:
        num+=1
