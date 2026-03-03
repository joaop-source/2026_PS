# ===============================================
# SISTEMA DE APROVAÇAO DE ALUNOS
# ===============================================
# Disciplina : Programação de Sistemas (PS)
# Aula       : 04 - Revisão de Python: Variáveis, Tipos de controle de fluxo
# Autor      : João Pedro Oliveira
# Data       : 24/02/2026
# Repositório: https://github.com/joaop-source/2026_PS.git
# ===============================================

# DESCRIÇÃO:
# Este programa processa as notas de uma turma e determina
# a situação de cada aluno (Aprovado, Reprovado ou Recuperação).
# Conceitos utilizados: variáveis, tipos de dados, operadores,
# estruturas de seleção e estruturas de repetição.
# ===============================================

# ---- DADOS DA TURMA ------------------------------
# Uma lista de dicionários, onde cada dicionário representa um aluno

turma = [
    {"nome": "Ana", "nota1": 8.0, "nota2": 7.5},
    {"nome": "Bruno", "nota1": 4.5, "nota2": 5.0},
    {"nome": "Carla", "nota1": 2.0, "nota2": 3.5},
]

print("=== Resultado da turma ===")
print()  # linha em branco para organizar saída

# o 'for' percorre cada aluno da lista automaticamente
for aluno in turma:

    nome = aluno["nome"]
    nota1 = aluno["nota1"]
    nota2 = aluno["nota2"]

    media = (nota1 + nota2) / 2  # operador aritmético: soma e divisão

    print()
    print(f"Aluno : {nome}")
    print(f"Nota 1 : {nota1:.1f}")
    print(f"Nota 2 : {nota2:.1f}")
    print(f"Média : {media:.2f}")   # :.2f = exibe com 2 casas decimais

    # ---- DECISÃO ----
    if media >= 6.0:  # condição principal
        situacao = "✅ Aprovado"

    elif media >= 4.0:  # condição alternativa (só verificada se a condição anterior for falsa)
        situacao = "⚠️ Recuperação"

    else:
        situacao = "❌ Reprovado"

    print(f"Situação : {situacao}")
    print("-" * 30)


continuar = "s"

while continuar == "s":

    print("\nDeseja processar outro aluno? (s/n) : ", end="")

    if continuar == "s":

        # complete aqui: peça nome, nota1 e nota2, calcule e exiba a situação

        nome = input("Nome do aluno: ")
        nota1 = float(input("Nota 1: "))
        nota2 = float(input("Nota 2: "))

        media = (nota1 + nota2) / 2  # cálculo da média

        print("\n=== Resultado ===")
        print(f"Aluno : {nome}")
        print(f"Nota 1 : {nota1:.1f}")
        print(f"Nota 2 : {nota2:.1f}")
        print(f"Média : {media:.2f}")

        # ---- DECISÃO ----
        if media >= 6.0:
            situacao = "✅ Aprovado"

        elif media >= 4.0:
            situacao = "⚠️ Recuperação"

        else:
            situacao = "❌ Reprovado"

        print(f"Situação : {situacao}")
        print("-" * 30)