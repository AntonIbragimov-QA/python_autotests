import json
import random
from urllib import response
import requests
host = 'https://pokemonbattle.me:9104'
token = '6eb340e88df45b0ea664276fe0ad5e20'

reg_trainers = requests.post(f'{host}/trainers/reg', json = {
    "trainer_token": token,
    "email": "0cy564@bloheyz.com",
    "password": "OlgaMiia2903"
}, headers = {'Content-Type': 'application/json'})

act_trainers = requests.post(f'{host}/trainers/confirm_email', json = {
    "trainer_token": token
}, headers = {'Content-Type': 'application/json'})

creat_pokemons = requests.post (f'{host}/pokemons', json = {
    "name": "generate",
    "photo": "generate"
}, headers = {'Content-Type': 'application/json', 'trainer_token': token})

print (creat_pokemons.json())

dict = json.loads (creat_pokemons.content)
meaning = dict ['id']

from faker import Faker
fake = Faker()
r = fake.first_name()
from random import randint
t = random.randint(100, 1008)

change_pokemon = requests.put (f'{host}/pokemons', json = {
    "pokemon_id": meaning,
    "name": r,
    "photo": f"https://dolnikov.ru/pokemons/albums/{t}.png"
}, headers = {'Content-Type': 'application/json', 'trainer_token': token}) 

print (change_pokemon.json())

catch_pok_pokebol = requests.post(f'{host}/trainers/add_pokeball', json = {
    "pokemon_id": meaning
}, headers = {'Content-Type': 'application/json', 'trainer_token': token})

print (catch_pok_pokebol.json())