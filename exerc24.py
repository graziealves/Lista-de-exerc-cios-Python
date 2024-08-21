print("\33[1;35;40mÁrea de um Quadrado.\33[m")

altura = float(input("Informe o valor da altura do quadrado: "))
base = float(input("Informe o valor da base do quadrado:  "))

if (altura != base ):
   print(" \33 1;31;40mEsta área não é de um quadrado!\33[m")

area = base * altura



print("\33[1;35;40m A área do quadrado é:\33[m", area )
