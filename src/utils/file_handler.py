import csv
import os


def write_to_csv(data, filename='mega_sena_resultados.csv', output_dir='data'):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    filepath = os.path.join(output_dir, filename)

    try:
        with open(filepath, 'w', newline='', encoding='utf-8') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(['Concurso', 'Data Sorteio', 'Bola 1',
                               'Bola 2', 'Bola 3', 'Bola 4', 'Bola 5', 'Bola 6'])
            for row in data:
                csvwriter.writerow(row)
        print(f"Data successfully written to {filepath}")
    except IOError as e:
        print(f"Error writing to CSV file {filepath}: {e}")
    except Exception as e:
        print(f"An unexpected error occurred during CSV writing: {e}")
