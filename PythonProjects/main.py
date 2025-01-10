import requests
URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '45a2b370183b9c6b461e1ab501899c28'
HEADER = {'Content-Type':'application/json',
          'trainer_token' : TOKEN
         }

body_create = {
    "name": "Hello",
    "photo_id": 953
 }

body_change = {
    "pokemon_id": "188371",
    "name": "NEWname",
    "photo_id": 5
}            

body_pokeball = {
    "pokemon_id": "188371"
}
'''response = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response.text)'''

'''response_change = requests.put(url = f'{URL}/pokemons',headers = HEADER, json = body_change)
print(response_change.text)'''

'''response_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pokeball )
print(response_pokeball.text)'''