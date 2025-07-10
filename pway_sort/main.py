import sys
import os
import tempfile

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
    heap = registros[:p]
    registros_restantes = registros[p:]
    run = []
    next_run = []
    while len(heap) != 0:        
        pos_menor = retorna_pos_menor(heap)
        if (len(run) == 0) or (heap[pos_menor] >= run[-1]):
            run.append(heap[pos_menor])
        else:
            next_run.append(heap[pos_menor])
        menor = heap[pos_menor]
        print("menor=", menor)
        print("run=", run)
        if len(registros_restantes) != 0:
            proximo = registros_restantes[0]
            print("próximo=", proximo)
        del heap[pos_menor]
        # if len(heap) == 0:
        #     break
        # pos_menor = retorna_pos_menor(heap)
        if len(registros_restantes) != 0:
            if (proximo >= menor):
                heap.append(proximo)
                print(f"{proximo} entra na heap")
            else:
                next_run.append(proximo)
                print(f"{proximo} vai para next_run")
            del registros_restantes[0]            
            print(f"heap={heap}")
    print("-----------------RUN GERADA-----------------")
    lista_run.append(run)
    if len(next_run) != 0:
        run_generator(p, next_run+registros_restantes, lista_run)
    print(f"lista_run = {lista_run}") 
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

def parses_generator(lista_run):
    lista_run = lista_run
    return "parses"

def write_output_file(output_file, registros):
    with open(output_file, 'w') as f:
        for reg in registros:
            f.write(f"{reg}\n")

def main():
    p, input_file, output_file = parse_args()
    registros = read_input_file(input_file)
    regs = len(registros)
    runs, lista_run = run_generator(p,registros)
    parses = parses_generator(lista_run)
    print(f"#Regs Ways #Runs Parses")
    print(f"{regs}  {p}    {runs}    {parses}")

if __name__ == "__main__":
    main()