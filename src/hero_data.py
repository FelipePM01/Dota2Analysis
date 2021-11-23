import requests,csv,json


def generate_heroes(arquivo1,arquivo2):
    url='https://raw.githubusercontent.com/odota/dotaconstants/master/build/heroes.json'
    json=requests.get(url)
    json=json.json()
    fieldnames=['id','nome','atributo_primario','tipo_ataque']
    fieldnames2=['nome','funcao']
    with open(arquivo1, mode='w') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for hero in json:
            print(hero)
            
            writer.writerow({'id':json[hero]['id'],'nome': json[hero]['localized_name'], 'atributo_primario': json[hero]['primary_attr'],'tipo_ataque':json[hero]['attack_type']})
    with open(arquivo2, mode='w') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames2)
        writer.writeheader()
        for hero in json:
            for role in json[hero]["roles"]:
                writer.writerow({'nome': json[hero]['localized_name'], "funcao":role})

def main():
    arq1='hero_data.csv'
    arq2='hero_role_data.csv'
    generate_heroes(arq1,arq2)
    
if __name__ == '__main__':
    main()