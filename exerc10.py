print("\33[1;35;40mAnálise de um Triângulo!\33[m")

lado1 = int(input("Informe o 1º lado:"))
lado2 = int(input("Informe o 2º lado:"))
lado3 = int(input("Informe o 3º lado:"))

if(lado1+lado2> lado3 and lado1+lado3 > lado2 and lado2+lado3 > lado1):
    if(lado1==lado2 and lado1==lado3):
        print("Triângulo Equilátero!")
    elif(lado1==lado2 or lado1==lado3 or lado2==lado3):
        print("Triângulo Isóceles!")
    else:
        print("Triângulo Escaleno!")
else:
    print("A medida dos lados não formam um triângulo.")