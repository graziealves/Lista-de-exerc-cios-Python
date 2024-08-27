numeros =[]
resultado=0
print("\33[1;35;40mCalculadora!\33[m\n")

for i in range(0,2):
    numeros.append(int(input(f"\33[1;35;40mDigite o {i+1}º número:\33[m")))

operador = (input(f"\33[1;35;40mDigite o operador desejado:\33[m"))
    
if (operador == "+"):
    resultado = numeros[0]+ numeros[1] 
elif(operador == "-"):
    resultado = numeros[0]- numeros[1]
elif(operador == "*"):
    resultado = numeros[0] * numeros[1]
elif(operador == "/" and numeros[1]!=0):
    resultado = numeros[0] / numeros[1]
elif(operador == "/" and numeros[1]==0):
    resultado = ("Informe um divisor diferente de zero.")
else:
    print("\33[1;31;40mOperador desconhecido!\33[m")

print("\33[1;35;40mO resultado é : \33[m",resultado)