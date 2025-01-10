import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '45a2b370183b9c6b461e1ab501899c28'
HEADER = {'Content-Type':'application/json',
          'trainer_token' : TOKEN
         }
ID = '13001'

def test_status_code():
    response = requests.get(url = f'{URL}/pokemons')
    assert response.status_code == 200

def test_part_of_response():
    response_get = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : ID})
    assert response_get.json()["data"][0]["trainer_id"] == ID



