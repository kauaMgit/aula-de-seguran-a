def gerar_padroes(N):
    for i in range(1, N + 1):
        # Linha crescente
        crescente = ' '.join(str(x) for x in range(1, i + 1))
        print(crescente)
        
        # Linha decrescente
        decrescente = ' '.join(str(x) for x in range(i, 0, -1))
        print(decrescente)

    # Linha decrescente completa
    for i in range(N - 1, 0, -1):
        # Linha crescente
        crescente = ' '.join(str(x) for x in range(1, i + 1))
        print(crescente)
        
        # Linha decrescente
        decrescente = ' '.join(str(x) for x in range(i, 0, -1))
        print(decrescente)

# Leitura da entrada
import sys
input = sys.stdin.read
N = int(input().strip())