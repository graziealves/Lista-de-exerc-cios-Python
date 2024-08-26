print("\33[1;31;40mRendimento.\33[m\n")

deposito = float(input("Informe o valor do depósito: R$"))
taxa = float(input("Informe o valor da taxa: %"))
rendimento = deposito * taxa 

print("\33[1;31;40mO seu rendimento foi:\33[m R$ ",rendimento)