import requests
import json

def request_json():
    api_response = requests.get('https://api.opendota.com/api/matches/271145478?api_key=YOUR_API_KEY')

    if api_response.status_code != 200:
        print("Erro ao realizar chamada!")

        return 0
    else:
        api_response_json = api_response.json()
        print(json.dumps(api_response_json, indent=3))

        matches = api_response_json["match_id"]

        #Construcao de um dicionario para melhor visualizacao
        #Precisa ser contruido com o index desejado
        '''
        index = ["Match_Id"]
        data_json_api = []
        for match in matches["match_id"]:
            if match["game_mode"] == 2 and match["human_players"] == 10:
                data_json_api.append(match["match_id"])


                zip_iterator = zip(index, data_json_api)

                a_dictionary = dict(zip_iterator)

                print(a_dictionary)

        return data_json_api
        '''
    return 0

def main():
    dicionario_json = request_json()
    return

if __name__ == '__main__':
    main()