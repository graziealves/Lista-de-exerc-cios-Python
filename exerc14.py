print("\33[1;31;40mAnálise sobre sexo.\33[m\n")

print("Informe 'F' para feminino.")
print("Informe 'M' para masculino.\n")

sexo = input("Informe o sexo: ")

if(sexo in 'fF'):
    print("\33[1;35;40mFeminino!\33[m")
elif(sexo in 'mM'):
    print("\33[1;34;40mMasculino!\33[m")
else:
    print("\33[1;31;40mInválido!\33[m")