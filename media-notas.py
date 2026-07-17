nota1 = int(input("digite sua primeira nota: "))
nota2 = int(input("digire sua segunda nota: "))

somanota = nota1 + nota2

media = somanota / 2

if media >= 7:
    print("Parabens! você foi aprovado")
else:
    print("que pena, você não passou")