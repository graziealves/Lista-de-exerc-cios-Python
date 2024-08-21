print("\33[1;31;40mAumento de Salário.\33[m")

salario = float(input("Informe o seu salario: R$: "))
aumento = salario * 0.05
salario = salario + aumento
imposto = salario * 0.07
salario = salario - imposto

print("\33[1;31;40mO seu salário atual é:\33[m R$", salario)