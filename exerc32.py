print("Graus\33[m \n")

fahrenheit = float(input("\33[1;35;40mInforme a temperatura em graus °C:\33[m")) 
kelvin = float(input("\33[1;35;40mInforme a temperatura em graus °C:\33[m")) 

fahrenheit = (fahrenheit * 1.8) + 32
kelvin = kelvin + 273.15

print("\33[1;35;40mA temperatura em fahrenheit é: \33[m", fahrenheit) 
print("\33[1;35;40mA temperatura em kelvin é: \33[m", kelvin) 
