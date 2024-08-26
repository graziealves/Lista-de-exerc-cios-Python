print("\33[1;35;40Turno Escolar!\33[m\n")

print("Digite \33[1;33;40m'M'\33[m para \33[1;33;40mMatituno\33[m.")
print("Digite \33[1;32;40m'V'\33[m para \33[1;32;40mVespertino\33[m.")
print("Digite \33[1;34;40m'N'\33[m para \33[1;34;40mNoturno\33[m.")

turno = input("Informe o seu turno escolar: ") [0]

if(turno in 'mM'):
    print("\33[1;33;40mBom dia!!\33[m")
elif(turno in 'vV'):
     print("\33[1;32;40mBoa Tarde!!\33[m")
elif(turno in 'nN'):
    print("\33[1;34;40mBoa Noite!!\33[m")
else:
    print("\33[1;31;40mTurno não inválido!\33[m")

