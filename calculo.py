def somar(op1, op2):
    r = op1 + op2
    return r

def subtrair(op1, op2):
    r = op1 - op2
    return r 

def multiplicar(op1, op2):
    r = op1 * op2
    return r 

def dividir (num, den):
    if den == 0 :
        return "infinito"

    else:
        r = num / den 
    return r 

def potencia(base, expoente):
    if base == 0 and expoente == 0:
        return "indeterminado"
    else:
          if expoente < 0:
               base = 1
               acumulador = 1
               for i in range(expoente):
                   acumulador = acumulador * base
    return acumulador


op1 = int(input("Digite o 1 número: "))
op2 = int(input("Digite o 2 número: "))
resultado = potencia(op1, op2)
print(f"resultado {resultado}") 