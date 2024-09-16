qtd_alunos = int(input("\33[1;35;40mInforme a quantidade de alunos do 2°DS: \33[m"))
alunos = []

for i in range (0,qtd_alunos):
  alunos.append(input(f"\33[1;37;40mInforme o nome do {i+1}º aluno:\33[m "))

print(f"\33[1;35;40mA lista de alunos do 2°DS é:\33[m \33[1;37;40m\n{alunos}\33[m")
