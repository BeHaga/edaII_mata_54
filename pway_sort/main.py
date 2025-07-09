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

def write_output_file(output_file, registros):
    with open(output_file, 'w') as f:
        for reg in registros:
            f.write(f"{reg}\n")

def main():
    p, input_file, output_file = parse_args()
    registros = read_input_file(input_file)
    print(f"#Regs Ways #Runs Parses")
    print(f"{len(registros)}  {p}    runs    parses")

if __name__ == "__main__":
    main()