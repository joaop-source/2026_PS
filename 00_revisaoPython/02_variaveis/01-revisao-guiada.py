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
    # ---- DECISÃO ----
    if media >= 6.0:  # condição principal
        situacao = "✅ Aprovado"

    elif media >= 4.0:  # condição alternativa (só verificada se a condição anterior for falsa)
        situacao = "⚠️ Recuperação"

    else:
        situacao = "❌ Reprovado"

    print(f"Aluno : {nome}")
    print(f"media : {media:.2f}")
    print(f"Situação : {situacao}")
    print("-" * 30)
continuar = "s"

while continuar == "s":
    print("\nDeseja processar outro aluno? (s/n): ", end="")
    continuar = input().lower()

    if continuar == "s":
        # complete aqui: peça nome, nota1 e nota2,
        # calcule e exiba a situação
        pass