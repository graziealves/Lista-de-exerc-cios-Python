numeros= []
print("\33[1;35;40mMultiplicação de números!\33[m")

for i in range(0,3):
    numeros.append(float(input(f"Informe o {i+1}º número: ")))

multiplicacao = (numeros[0] * numeros[1])* numeros[2]

print("\33[1;35;40mA multiplicação desses números é: \33[m", multiplicacao)