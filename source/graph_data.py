import csv

def insert_jogador(arquivo,nome,mmr,rank,id,taxa):
    fieldnames = ['nome', 'mmr', 'rank','id','taxa']
    encontrado=False
    with open('employee_birthday.txt', mode='r') as csv_file:
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
            writer.writerow({'nome': str(nome), 'mmr': str(mmr), 'id': str(id),'rank':str(rank), 'taxa': str(taxa)})

        
   