import requests
import json
import csv
import time


def read_csv():
    visited_matches = []
    with open('data/processed/performance_data.csv') as dota_data_file:
        csv_reader = csv.reader(dota_data_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                if row:
                    visited_matches.append(row[0])
                    line_count += 1
        print(f'Processed {line_count} lines.')
    print(visited_matches)
    return visited_matches

def get_new_matches_ids(visited_matches):
    new_ids = []
    with open('data/processed/match_data.csv') as dota_data_file:
        csv_reader = csv.reader(dota_data_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                if row:
                    if row[0] not in visited_matches:
                        new_ids.append(row[0])
                    line_count += 1
        print(f'Processed {line_count} lines.')

    return new_ids

def write_csv(new_ids):
    with open('data/processed/performance_data.csv', mode='a') as dota_data_file:
        dota_data_writer = csv.writer(dota_data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        for id in new_ids:
            api_player_info = requests.get(
                'https://api.opendota.com/api/matches/' + str(id) + '?api_key=220935B4AB4C12F87AB7B4CB62D6CFBB')

            if api_player_info.status_code != 200:
                print("API Request Error! Player info not found")
                time.sleep(.2)
            else:
                player_info = api_player_info.json()

                for player in range(0, 10):
                    radiant_team = True
                    if player_info["players"][player]["account_id"] is not None:
                        if player_info["players"][player]["player_slot"] > 4:
                            radiant_team = False

                        damage_taken = player_info["players"][player]["damage_taken"]
                        damage_taken_sum = 0
                        if damage_taken is not None:
                            for key, value in damage_taken.items():
                                if "npc_dota_hero" in key:
                                    damage_taken_sum += value

                        dota_data_writer.writerow(
                            [id, player_info["players"][player]["account_id"], radiant_team, player_info["players"][player]["level"], player_info["players"][player]["hero_id"], player_info["players"][player]["hero_damage"], player_info["players"][player]["hero_healing"], damage_taken_sum, player_info["players"][player]["tower_damage"],\
                             player_info["players"][player]["kills"], player_info["players"][player]["assists"], player_info["players"][player]["deaths"], player_info["players"][player]["kda"],\
                             player_info["players"][player]["gold_per_min"], player_info["players"][player]["gold_spent"], player_info["players"][player]["xp_per_min"], player_info["players"][player]["last_hits"],\
                             player_info["players"][player]["item_0"], player_info["players"][player]["item_1"], player_info["players"][player]["item_2"], player_info["players"][player]["item_3"], player_info["players"][player]["item_4"], player_info["players"][player]["win"]])
                        print("New performance added to database by: " + str(player_info["players"][player]["account_id"]))
                    time.sleep(.5)
            time.sleep(.5)

def main():
    visitated_players = read_csv()
    time.sleep(1)
    new_players = get_new_matches_ids(visitated_players)
    time.sleep(1)
    write_csv(new_players)

    return


if __name__ == '__main__':
    main()