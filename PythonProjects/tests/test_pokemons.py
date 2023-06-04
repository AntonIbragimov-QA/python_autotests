import requests
import pytest

host = 'https://pokemonbattle.me:9104'
token = '6eb340e88df45b0ea664276fe0ad5e20'

@pytest.mark.parametrize('key, value',[("city", "Ufa"),
                                        ("trainer_name", "AntonIndiana")])

def test_body(key, value):
    info_trainers = requests.get(f'{host}/trainers', 
                                 params = {'trainer_id':4638})
    assert info_trainers.json()[key] == value
   

def test_body_code():
    info_trainers = requests.get(f'{host}/trainers', 
                                 params = {'trainer_id':4638})
    assert info_trainers.status_code == 200