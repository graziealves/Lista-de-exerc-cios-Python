numeros =[]

print("Calculadora simples!")

for i in range(0,2):
    numeros.append(int(input(f"Digite o {i+1}º número: ")))

operador = (input(f"Digite o operador desejado + ou - : "))
    
if (operador == "+"):
    resultado = numeros [0]+ numeros [1] 
elif(operador == "-"):
    resultado = numeros [0]- numeros [1]
else:
    print("Operador desconhecido!")
print("O resultado é : " , resultado)