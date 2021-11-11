import csv

def insert_jogador(arquivo,id,mmr,rank):
    fieldnames = ['id', 'mmr', 'rank']
    encontrado=False
    with open(arquivo, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for row in csv_reader:
            if line_count != 0:
                if row['id']==id:
                    encontrado=True
                line_count+=1
    if not encontrado:
        with open(arquivo, mode='w') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow({'id': str(id), 'mmr': str(mmr),'rank':str(rank)})


def create_jogador(arquivo,id1,id2):
    fieldnames = ['jogador 1', 'jogador 2']
    encontrado=False
    with open(arquivo, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        linha=0
        for row in csv_reader:
            if line_count != 0:
                if row['jogador1']==id1 and row['jogador2']==id2:
                    encontrado=True
                    linha=line_count
                line_count+=1
    if not encontrado:
        with open(arquivo, mode='w') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow({'jogador 1': str(id1), 'jogador 2': str(id2)})
