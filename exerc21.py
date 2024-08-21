import math

print("\33[1;35;40mEquação de Segundo Grau\33[m")

a = int(input("Informe o valor de \33[1;35;40mA\33[m: "))
b = int(input("Informe o valor de \33[1;35;40mB\33[m: "))
c = int(input("Informe o valor de \33[1;35;40mC\33[m: "))

if(a!=0 and b!=0 and c!=0):
    delta = (b * b) * -4 * a * c
    x1 = (-b + math.isqrt(delta)) / (2 * a)
    x2 = (-b - math.isqrt(delta)) / (2 * a)
    print("A raíz quadrada de 'X1' é de: {0:.1f}".format(x1))
    print("A raíz quadrada de 'X2' é de: {0:.1f}".format(x2))
else:
   print("\33[1;31;40mNão é uma equação de 2º grau!!\33[m")