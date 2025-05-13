Peso = float(input("digite o peso"))
Altura = float(input("Digite a altura"))
media = Peso/(Altura**2)

print(media)
if media >= 10.5 and media <=18:
    print ("Abaixo do peso") 

if media >=18.5 and media <=24.9:
    print("Peso normal")

if media >=24.9 and media <=29.9:
    print("Sobrepeso")

if media >=29.9 and media <=35.9:
    print("Obesidade")

if media >= 35.9 and media <=200:
    print("Obesidade II")