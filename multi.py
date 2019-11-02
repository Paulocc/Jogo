n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
resul = n1*n2
print("O resultado é: ", resul)
for x in range(resul):
    for i in range(resul):
        if (resul-x) == resul or (resul-x) == 1:
            print("*", end="")
        else:        
            if (resul-i) == resul or (resul-i) == 1:
                print("*", end="")
            else:
                print(" ", end="") 
    print()
