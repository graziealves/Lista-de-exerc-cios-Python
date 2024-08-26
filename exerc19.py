print("\33[1;35;40mNúmeros em ordem decrescente.\33[m\n")

numeros=[]

for i in range(0,3):
    numeros.append(int(input(f"Digite o {i+1}º número: ")))

numeros.sort(reverse = True)
print("\33[1;35;40mA ordem decrescente destes números são:\33[m ", numeros)












































