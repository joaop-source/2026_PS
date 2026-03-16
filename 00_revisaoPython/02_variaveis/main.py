
import time


def Soma(n1, n2):
    return(n1 + n2)

def Diminuição(n1, n2):
    return(n1-n2)

def Multiplicação(n1, n2):
    return(n1 * n2)

def Divisão(n1, n2):
    return(n1 / n2)


def escreva(msg, resultado):    
    print(f'{msg} = {resultado}')

    
def executar_linha(atraso=0.8):
    """Simula o processamento da linha."""
    print(f"⚙️  [Lendo Linha ]...", end="\r")
    time.sleep(atraso)
    print(f"✅ [Executado Linha ]   ")


print("Bem vindo a calculadora")
time.sleep(1)
n1 = int(input("digite um numero: "))
executar_linha(2)
n2 = int(input("digite outro numero: "))
executar_linha(3)
op = input("digite uma operação (+, -, *, /): ")
executar_linha(4)

print("seu resultado é:")
time.sleep(1)

msg =  f"{n1} {op} {n2}"
if op == '+':
    res = Soma(n1, n2)
elif op == '-':
    res = Diminuição(n1, n2)
elif op == '*':
    res = Multiplicação(n1, n2)
elif op == '/':
    res = Divisão(n1, n2)
else:
    res = "operação invalida"
escreva(msg, res)
print("obrigado por usar a calculadora")
time.sleep(1)
print("volte sempre")
time.sleep(1)