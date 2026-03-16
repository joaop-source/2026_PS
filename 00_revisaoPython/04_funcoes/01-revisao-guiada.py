# ==================================================
# SISTEMA DE CÁLCULO DE IMC
# ==================================================
# Disciplina : Programação de Sistemas (PS)
# Aula       : 06 - Revisão: Funções
# Autor      : João Pedro Oliveira
# Data       : 24/02/2026
# Repositório: https://github.com/joaop-source/2026_PS.git
# ==================================================
#
# DESCRIÇÃO:
# Calcula e classifica o IMC de uma pessoa.
# Demonstra definição de funções, parâmetros,
# retorno, escopo e recursão.
# ==================================================


# ---- FUNÇÃO SEM PARÂMETROS E SEM RETORNO ----

def exibir_cabecalho():
    """Exibe o cabeçalho do sistema no terminal."""  # docstring: documentação da função

    print("=" * 40)
    print("   SISTEMA DE CÁLCULO DE IMC")
    print("=" * 40)


# Chamando a função
exibir_cabecalho()
# ---- FUNÇÃO COM PARÂMETROS E RETORNO ----

def calcular_imc(peso, altura):
    """Calcula e retorna o IMC. Fórmula: peso / altura²"""

    imc = peso / (altura ** 2)  # ** é o operador de potência
    return imc                  # devolve o resultado para quem chamou


# Coletando dados do usuário
peso = float(input("Peso (kg): "))
altura = float(input("Altura (m): "))


# Chamando a função e armazenando o retorno
resultado = calcular_imc(peso, altura)

print(f"Seu IMC é: {resultado:.2f}")
# ---- ESCOPO LOCAL vs. GLOBAL ----

versao = "1.0"   # variável GLOBAL — existe fora de qualquer função


def demonstrar_escopo():

    mensagem = "Olá do interior da função"   # variável LOCAL

    print("Dentro da função:")
    print(f"   mensagem = {mensagem}")       # OK: local existe aqui
    print(f"   versao   = {versao}")         # OK: global é visível dentro


demonstrar_escopo()

print("\nFora da função:")
print(f"   versao = {versao}")               # OK: global existe aqui
# print(mensagem)                           # ERRO: local não existe aqui!