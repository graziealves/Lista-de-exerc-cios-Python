print("\33[1;35;40mPar ou ímpar??.\33[m\n")

numero = int(input("Informe um número: "))

if(numero%2 == 0):
    print("Este número é \33[1;35;40mPAR!!\33[m")
else:
    print("Este número é \33[1;35;40mÍMPAR!!\33[m")