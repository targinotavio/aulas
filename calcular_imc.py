p = float(input("Digite seu peso(kg): "))
a = float(input("Digite sua altura(M): "))

def potencia(p, a):
    peso = p
    altura = a
    
    imc = peso / (altura * altura) 

    if imc < 18.5:
        print("Abaixo do peso!")
    else:
        print("peso adequado")
    return imc

resultado = potencia (p, a)
print(f"resultado {resultado}")