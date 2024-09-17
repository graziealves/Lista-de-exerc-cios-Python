nomes = []
notas = []

boletim = []

for i in range(0, 4):
  nome = input(f"Informe o nome do {i+1}º aluno: ")
  nomes.append(nome)
  notas = []
  for n in range(0, 4):
    notas.append(float(input(f"Informe a nota do {n+1}º bimestre do aluno(a) {nome}: ")))
  notas.insert(0, nome)
  boletim.append(notas)

for a in range (0,4):
  boletim[nomes[a]][]

print(boletim)