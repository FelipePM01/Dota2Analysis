import requests
import json
import csv
import time

def read_csv():
    visited_matches = []
    with open('match_data.csv') as dota_data_file:
        csv_reader = csv.reader(dota_data_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                if row:
                    visited_matches.append(int(row[0]))
                    line_count += 1
        print(f'Processed {line_count} lines.')

    return visited_matches

def get_new_match_ids(visited_matches):
    api_response = requests.get('https://api.opendota.com/api/publicmatches?api_key=220935B4AB4C12F87AB7B4CB62D6CFBB')

    if api_response.status_code != 200:
        print("API Request Error - Public Matches not found")

        return 0
    else:
        public_matches = api_response.json()

        public_matches_info = []

        for match in public_matches:
            if match["game_mode"] == 22 and match["avg_mmr"] is not None:
                if match["match_id"] not in visited_matches:
                    match_info = []
                    match_info.append(match["match_id"])
                    match_info.append(match["avg_mmr"])

                    public_matches_info.append(match_info)
                    print("New match found: " + str(match["match_id"]))

        return public_matches_info

def write_csv(new_matches):
    with open('match_data.csv', mode='a') as dota_data_file:
        dota_data_writer = csv.writer(dota_data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        for match in new_matches:
            api_match_info = requests.get(
                'https://api.opendota.com/api/matches/' + str(match[0]) + '?api_key=220935B4AB4C12F87AB7B4CB62D6CFBB')

            if api_match_info.status_code != 200:
                print("API Request Error! Match info not found")
                time.sleep(.2)
                return 0
            else:
                match_info = api_match_info.json()

                dota_data_writer.writerow([match[0], match[1], match_info["players"][0]["account_id"], match_info["players"][1]["account_id"],match_info["players"][2]["account_id"],match_info["players"][3]["account_id"],match_info["players"][4]["account_id"],\
                                           match_info["players"][5]["account_id"], match_info["players"][6]["account_id"],match_info["players"][7]["account_id"],match_info["players"][8]["account_id"],match_info["players"][9]["account_id"],\
                                           match_info["radiant_win"], match_info["first_blood_time"], match_info["duration"]])
                print("New match added to database: " + str(match[0]))
                time.sleep(.2)


def main():
    for i in range(0, 50):
        visited_matches = read_csv()
        time.sleep(1)
        new_matches = get_new_match_ids(visited_matches)
        time.sleep(1)
        write_csv(new_matches)
        time.sleep(30)
    return

if __name__ == '__main__':
    main()