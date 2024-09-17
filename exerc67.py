tabela = dict()

quantidade = 2
desempenho = []
for i in range(0,quantidade):
   time = input("\33[1;37;40mInforme o nome do time: \33[m")
   if time not in tabela:
    for c in range(0,7):
        if c == 1:
            info = int(input ("Informe a quantidade de vitórias: "))
        elif c == 2:
            info = int(input ("Informe a quantidade de empates: ")  
          pare
          caso 3:
            escreva ("Informe a quantidade de derrotas: ") 
            leia(tabela[l][c])  
            pare
          caso 4:
            escreva ("Informe a quantidade de gols próprios: ")  
            leia(tabela[l][c])  
          pare
          caso 5:
            escreva ("Informe a quantidade de gols contras: ")  
            leia(tabela[l][c])  
          pare
          caso 6:
            tabela[l][c] = tabela[l][c-2]-tabela[l][c-1]
          pare
          escreva("\n")        
        info = int(input("Informe a informação ")  )
        desempenho.append(info)
    tabela[time] = desempenho
    desempenho = []

print(tabela)


