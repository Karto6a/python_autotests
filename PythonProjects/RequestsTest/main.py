import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'd16f220cf5f59f4bd0c17b4036778f35'
HEADER = {'Content-Type' : 'application/json' , 'trainer_token' : TOKEN}
BODY_POKEMON = {
    "name": "Автотестусы",
    "photo_id": 1
}


response = requests.post(url=f'{URL}/pokemons', headers = HEADER, json = BODY_POKEMON)
print (response.text)

POKEMON_ID = response.json () ['id']


BODY_CHANGE = {
    "pokemon_id": POKEMON_ID,
    "name": "Автотесты",
    "photo_id": 2
}

response2 = requests.put(url=f'{URL}/pokemons', headers = HEADER, json = BODY_CHANGE)

print (response2.text)

BODY_POKEBALL = {
    "pokemon_id": POKEMON_ID
}

response3 = requests.post(url=f'{URL}/trainers/add_pokeball', headers = HEADER, json = BODY_POKEBALL)
print (response3.text)
