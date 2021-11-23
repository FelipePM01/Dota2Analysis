import requests
import json
import csv
import time
from itertools import combinations


def read_csv():
    visited_matches = []
    with open('data/processed/graph_data.csv') as dota_data_file:
        csv_reader = csv.reader(dota_data_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                if row and row not in visited_matches:
                    visited_matches.append(row[0])
                    line_count += 1
        print(f'Processed {line_count} lines.')

    return visited_matches

def get_new_two_player_ids(visited_matches):
    with open('data/processed/match_data.csv') as dota_data_file:
        csv_reader = csv.reader(dota_data_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                if row:
                    players_in_match = []
                    if row[0] not in visited_matches:
                        visited_matches.append(int(row[0]))

                        for column in range(2,12):
                            if row[column] != "":
                                players_in_match.append(int(row[column]))

                        duo_id_list = list(combinations(players_in_match, 2))

                        create_jogador(row[0], duo_id_list)

                        line_count += 1
        print(f'Processed {line_count} lines.')


def create_jogador(match_id, duo_id_list):
    with open('data/processed/graph_data.csv', mode='a') as dota_data_file:
        dota_data_writer = csv.writer(dota_data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        for duo in duo_id_list:
            dota_data_writer.writerow([match_id, duo[0], duo[1]])

def ocorrencies_count():
    return

def main():
    visitated_matches = read_csv()
    time.sleep(1)
    get_new_two_player_ids(visitated_matches)

    ocorrencies_count()
    return


if __name__ == '__main__':
    main()