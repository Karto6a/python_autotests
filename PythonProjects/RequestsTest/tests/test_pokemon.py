import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'd16f220cf5f59f4bd0c17b4036778f35'
HEADER = {'Content-Type' : 'application/json' , 'trainer_token' : TOKEN}
TRAINER_ID = '4373'

def test_status_code ():
    response = requests.get(url = f'{URL}/trainers')
    assert response.status_code == 200

def test_name_mytrener ():
    response_name = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response_name.json () ["data"] [0] ["trainer_name"] == 'Картоша'


 