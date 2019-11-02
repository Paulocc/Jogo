a=int(input())
b=int(input())
soma=a+b
print(soma)
if soma>1:
	for i in range (1,soma):
		if i!=1 and soma%i==0:
			print(soma,"não é primo")
			break
	if i==soma-1 or soma==2:
		print(soma,"é primo")
else:
	print("Entrada inválida")
