import csv

def write_to_csv(data, filename='Data.csv'):
    with open(filename, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        # Escreve o cabeçalho
        csvwriter.writerow(['Concurso', 'Dia', 'Bola 1', 'Bola 2', 'Bola 3', 'Bola 4', 'Bola 5', 'Bola 6'])
        for row in data:
            csvwriter.writerow(row)