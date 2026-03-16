# debug_teste/01b-debug.py
# ATENÇÃO: 4 erros propositais. Encontre e corrija todos!
# Rode de dentro de 05_modulos/: python debug_teste/01b-debug.py

import Temperatura
# ERRO 1: módulo com nome incorreto.
# O arquivo correto é conversores/temperatura.py.
# Python diferencia maiúsculas e minúsculas.
# Correto seria: from conversores import temperatura

from conversores import celsius_para_kelvin, converter_distancia
# ERRO 2: converter_distancia não existe no pacote conversores.

resultado = celsius_para_kelvin(25)
print(f"25°C em K: {resultado}")

from utils.formatador import formatar_resultado

print(formatar_resultado("teste", 100, "km", 62.1, "mi", "extra"))
# ERRO 3: número de argumentos errado.
# formatar_resultado() aceita 5 parâmetros, mas foram passados 6.

from conversores import km_para_milhas

print(f"50 km = {km_para_milhas(50):.2f} mi")

from debug_teste import algo
# ERRO 4: não existe módulo ou função chamada "algo" em debug_teste.