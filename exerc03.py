numeros=[]

for i in range(0,3):
    numeros.append(int(input(f"Digite o {i+1}º número: ")))

soma = numeros[0] + numeros[1] + numeros[2] 

print (f"O valor da soma é de: {soma}")
