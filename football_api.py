import requests

api_key = "3"

url = "https://www.thesportsdb.com/api/v1/json/3/search_all_teams.php?l=English%20Premier%20League"

headers = {
    "apikey": api_key
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()

else:
    print("Error:", response.status_code)

if response.status_code == 200:
    data = response.json()
    teams = data["teams"]
    
    for team in teams:
        print("Team name:", team["strTeam"])
else:
    print("Error:", response.status_code)
