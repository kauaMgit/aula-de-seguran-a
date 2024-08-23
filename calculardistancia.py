def calcular_distancia(t, v):
    if 1 <= t <= 100 and 0 <= v <= 120:
        return t * v
    elif t == 0 and v == 0 :
        return 0
    else:
        return -1 #indica entrada inválida

#leitura dos intervalos
t1, v1 = map(int, input('digite o tempo e a velocidade para o intervalo 1(separado por espaço):').split())
t2, v2 = map(int, input('digite o tempo e a velocidade para o intervalo 1(separado por espaço):').split())
t3, v3 = map(int, input('digite o tempo e a velocidade para o intervalo 1(separado por espaço):').split())

#calculo das distancia para cada intervalo
distancia1 = calcular_distancia(t1, v1)
distancia2 = calcular_distancia(t2, v2)
distancia3 = calcular_distancia(t3, v3)

#verificação de intradas invalidas
if distancia1 == -1  or distancia2 == -1 or distancia3 == -1:
    print('entrada invalida')
else:
    distancia_total = distancia1 + distancia2 + distancia3
    print('distancia total percorrida:', distancia_total)