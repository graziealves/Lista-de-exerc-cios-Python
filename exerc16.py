print("\33[1;31;40mAumento de Salário.\33[m")

salario = float(input("Informe o seu salario R$: "))
percentual = float(input("Informe o percentual: "))
percentual = percentual / 100
aumento = salario * percentual
novos = salario + aumento

print(f"\n\33[1;31;40mSalário Novo:\33[m R$", novos)

