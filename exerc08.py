letra = input ("\33[1;35;40mInforme uma letra: \33[m")[0]

if(letra in "aeiou" ):
    print("\33[1;37;40mEsta Letra é uma\33[m \33[1;35;40mVogal!\33[m")
else:
    print("\33[1;37;40mEsta Letra é uma\33[m \33[1;35;40mConsoante!\33[m")