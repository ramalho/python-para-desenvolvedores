# Módulo para matemática
import math

# Módulo para matemática (de complexos)
import cmath

# Complexos
for cpx in [3j, 1.5 + 1j, -2 - 2j]:
    # Conversão para coordenadas polares
    plr = cmath.polar(cpx)
    print('Complexo:', cpx)
    print('Forma polar:', plr, '(em radianos)')
    print('Amplitude:', abs(cpx))
    print('Ângulo:', math.degrees(plr[1]), '(graus)')
