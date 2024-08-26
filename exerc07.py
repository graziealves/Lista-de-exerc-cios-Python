notas= []
print("\33[1;35;40mCálculo de média de notas!\33[m")
materias = str (input("Informe a disciplina: "))

for i in range(0,4):
    notas.append(float(input(f"Informe a {i+1}º nota: ")))

media = (notas[0] + notas[1] + notas[2] + notas[3]) /4

if media >=7:
    print("Você foi aprovado!!")
else:
    ("Você foi reprovado!!")

print("A sua média é: ", media)
print(materias)