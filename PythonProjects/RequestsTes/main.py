import requests

token = '65752cc003b73e6c15680a7fa1550f6a'

response = requests.post('https://pokemonbattle.me:9104/pokemons', headers = {'Content-Type': 'application/json', 'trainer_token': token},
json= {"name": "Чармандер","photo": "https://dolnikov.ru/pokemons/albums/004.png"})
print(response.text)


response_change = requests.put('https://pokemonbattle.me:9104/pokemons', headers = {'Content-Type': 'application/json', 'trainer_token': token}, 
json = {"pokemon_id": 6109, "name": "Чарлик", "photo": "https://dolnikov.ru/pokemons/albums/004.png"})
print(response_change.text)



response_catch = requests.post('https://pokemonbattle.me:9104/trainers/add_pokeball', headers = {'Content-Type': 'application/json', 'trainer_token': token},
json= {"pokemon_id": 6109})
print(response_catch.text)

