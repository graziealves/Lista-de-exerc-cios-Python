print("\33[1;31;40mAumento de salário!\33[m\n")

salario = float(input("Informe o seu salario R$: "))
aumento = salario * 0.25
novos = salario + aumento 

print(f"Salário Antigo: R$",salario)
print(f"O seu aumento foi de: R$", aumento)
print(f"Salário Novo: R$", novos)
