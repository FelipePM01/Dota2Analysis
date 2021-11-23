import requests
import json
import csv
import time


def read_csv():
    visited_players = []
    with open('player_data.csv') as dota_data_file:
        csv_reader = csv.reader(dota_data_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                if row:
                    visited_players.append(row[0])
                    line_count += 1
        print(f'Processed {line_count} lines.')
    print(visited_players)
    return visited_players

def get_new_player_ids(visited_players):
    new_ids = []
    with open('match_data.csv') as dota_data_file:
        csv_reader = csv.reader(dota_data_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                if row:
                    for column in range(2,12):
                        if row[column] != "" and row[column] not in visited_players:
                            new_ids.append(int(row[column]))
                            visited_players.append(int(row[column]))
                    line_count += 1
        print(f'Processed {line_count} lines.')

    return new_ids

def write_csv(new_ids):
    with open('player_data.csv', mode='a') as dota_data_file:
        dota_data_writer = csv.writer(dota_data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        for id in new_ids:
            api_player_info = requests.get(
                'https://api.opendota.com/api/players/' + str(id) + '?api_key=220935B4AB4C12F87AB7B4CB62D6CFBB')

            if api_player_info.status_code != 200:
                print("API Request Error! Player info not found")
                time.sleep(.2)
            else:
                player_info = api_player_info.json()

                dota_data_writer.writerow(
                    [player_info["profile"]["account_id"], player_info["mmr_estimate"]["estimate"], player_info["rank_tier"]])
                print("New player added to database: " + str(id))
                time.sleep(.2)
            time.sleep(.5)

def main():
    visitated_players = read_csv()
    time.sleep(1)
    new_players = get_new_player_ids(visitated_players)
    time.sleep(1)
    write_csv(new_players)

    return


if __name__ == '__main__':
    main()