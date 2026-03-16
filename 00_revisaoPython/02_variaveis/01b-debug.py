# Arquivo: 01b-debug.py
# ATENÇÃO: Este código contém 4 erros propositais. Encontre e corrija todos!

nome = imput("Digite o nome do aluno: ")

nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))

media = nota1 + nota2 / 2

if media => 6.0:
    situacao = "Aprovado"

elif media >= 4.0:
    situacao = "Recuperação"

    else:
        situacao = "Reprovado"

pront(f"Aluno: {nome} | Média: {media:.2f} | Situação: {situacao}")
# Erros:
# 1. imput -> input
# 2. media = nota1 + nota2 / 2 -> media = (nota1 + nota2) / 2
# 3. if media => 6.0 -> if media >= 6.0
# 4. else: -> deve estar alinhado