print("\33[1;35;40mFibonacci!! \33[m")

contador= 3
numero1 = 1
numero2= 1
numero3 = 3 
fibonacci = int(input("\33[1;35;40mInforme um número:\33[m"))

while( contador <= fibonacci ):
    numero3 = numero1 + numero2
    numero1 = numero2
    numero2 = numero3
    contador = contador + 1

print("\33[1;35;40mA sua sequência fibonacci é:\33[m ", numero3)


