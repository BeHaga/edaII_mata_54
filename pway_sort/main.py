import sys
import os
import tempfile
from math import log, ceil

def parse_args():
    if len(sys.argv) != 4:
        print("Uso: python main.py <p> <input_file> <output_file>")
        sys.exit(1)
    try:
        p = int(sys.argv[1])
        if p < 2:
            raise ValueError
    except ValueError:
        print("Erro: p deve ser um inteiro >= 2.")
        sys.exit(1)
    input_file = sys.argv[2]
    output_file = sys.argv[3]
    if not os.path.isfile(input_file):
        print(f"Erro: Arquivo de entrada '{input_file}' não encontrado.")
        sys.exit(1)
    return p, input_file, output_file

def read_input_file(input_file):
    registros = []
    with open(input_file, 'r') as f:
        for line in f:
            tokens = line.strip().split()
            registros.extend(int(token) for token in tokens if token)
    return registros

def run_generator(p, registros, lista_run = None):
    if lista_run is None:
        lista_run = []
    restante = registros
    while restante:
        heap = restante[:p]
        registros_restantes = restante[p:]
        run = []
        next_run = []

        while len(heap) != 0:        
            pos_menor = retorna_pos_menor(heap)
            if (len(run) == 0) or (heap[pos_menor] >= run[-1]):
                run.append(heap[pos_menor])
            else:
                next_run.append(heap[pos_menor])
            menor = heap[pos_menor]
            # print("menor=", menor)
            # print("run=", run)
            if len(registros_restantes) != 0:
                proximo = registros_restantes[0]
                # print("próximo=", proximo)
            del heap[pos_menor]
            if len(registros_restantes) != 0:
                if (proximo >= menor):
                    heap.append(proximo)
                    # print(f"{proximo} entra na heap")
                else:
                    next_run.append(proximo)
                    # print(f"{proximo} vai para next_run")
                del registros_restantes[0]            
                # print(f"heap={heap}")

        # print("-----------------RUN GERADA-----------------")
        lista_run.append(run)
        restante = next_run+registros_restantes
            
    # print(f"lista_run = {lista_run}") 
    return len(lista_run), lista_run

def retorna_pos_menor(heap):
    menor = heap[0]
    pos = 0
    if len(heap) == 1:
        return 0
    for i in range(1, len(heap)):
        if heap[i] < menor:
            menor = heap[i]
            pos = i
    return pos

def parses_generator(runs, p):
    parses = ceil(log(runs, p))
    return parses

def p_way_merge(lista_run, regs):
    resultado_ordenado = []
    posicoes = [0] * len(lista_run)

    while len(resultado_ordenado) < regs:
        menor_valor = None
        idx_menor = -1

        for idx, run in enumerate(lista_run):
            pos = posicoes[idx]
            if pos < len(run):
                valor_atual = run[pos]
                if menor_valor is None or valor_atual < menor_valor:
                    menor_valor = valor_atual
                    idx_menor = idx

        resultado_ordenado.append(menor_valor)
        posicoes[idx_menor] += 1

    return resultado_ordenado

def write_output_file(output_file, registros):
    with open(output_file, 'w') as f:
        for reg in registros:
            f.write(' '.join(str(reg) for reg in registros))

def main():
    p, input_file, output_file = parse_args()
    registros = read_input_file(input_file)
    regs = len(registros)
    runs, lista_run = run_generator(p,registros)
    parses = parses_generator(runs, p)
    ordenado_final = p_way_merge(lista_run, regs)
    write_output_file(output_file, ordenado_final)
    print(ordenado_final)
    print(f"#Regs Ways #Runs Parses")
    print(f"{regs}  {p}    {runs}    {parses}")

if __name__ == "__main__":
    main()