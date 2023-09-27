import math
angulo = float(input("informe o valor do angulo: "))
angulo = math.radians(angulo)
#para converter em seno cosseno e tangente, os numeros precisao ser convetidos primeiro para radianos
print (f"o seno de {angulo:.2f} é {math.sin(angulo):.2f} o cosseno é {math.cos(angulo):.2f} e a tangente é {math.tan(angulo):.2f}")