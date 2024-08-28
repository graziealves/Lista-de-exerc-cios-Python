numeros = []

print("\33[1;35;40mSoma e média.\33[m")
for i in range(5):
    numeros.append(float(input(f"\33[1;37;40mInforme o {i +1} números: \33[m \n")))

soma = sum(numeros)
media = soma /5

print("\33[1;37;40mA soma desses números é: \33[m", soma)
print("\33[1;37;40mA mádia desses números é: \33[m", media)