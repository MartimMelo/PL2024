import math
import re
from collections import defaultdict

def processar_dados(linhas):
    
    modalidades = set()
    aptos = 0
    inaptos = 0
    escaloes = defaultdict(int)  # Inicializa escaloes como defaultdict de inteiros
    
    for linha in linhas[1:]:
        
        elementos = linha.split(",")

        idade = elementos[5].strip()
        modalidade = elementos[8].strip()
        resultado = elementos[12].strip()
        
        modalidades.add(modalidade)

        if resultado == 'true':
            aptos += 1
        else: 
            inaptos += 1
            
        i = math.floor(int(idade)/5)
        escaloes[i] += 1

    return modalidades, aptos, inaptos, escaloes

def calcular_faixa(i):
    x = 5 * i - 4
    y = 5 * i
    return f"[{x} - {y}]"

def imprimir_outputs(modalidades, aptos, inaptos, escaloes):
    
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'  
    
    print(HEADER + "1) Lista ordenada alfabeticamente das modalidades desportivas:" + ENDC)
    for index, modalidade in enumerate(sorted(modalidades)):
        print(f"{index+1}. {OKBLUE}{modalidade}{ENDC}")

    print(HEADER + "\n2) Percentagens de atletas aptos e inaptos para a prática desportiva:" + ENDC)
    total = aptos + inaptos
    print(f"Aptos: {OKGREEN}{aptos / total * 100:.2f}%{ENDC}")
    print(f"Inaptos: {FAIL}{inaptos / total * 100:.2f}%{ENDC}")

    print(HEADER + "\n3) Distribuição de atletas por escalão etário:" + ENDC)
    for escalao, count in escaloes.items():
        print(f"{calcular_faixa(escalao)}: {WARNING}{count}{ENDC}")


if __name__ == "__main__":

    with open('emd.csv', 'r') as f:
        modalidades, aptos, inaptos, escaloes = processar_dados(f.readlines())
        imprimir_outputs(modalidades, aptos, inaptos, escaloes)
