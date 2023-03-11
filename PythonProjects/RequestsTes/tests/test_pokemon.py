import requests
import pytest

def test_check_status_code():
    response = requests.get('https://pokemonbattle.me:9104/trainers')
    assert response.status_code == 200


def test_name_trainer():
    response = requests.get('https://pokemonbattle.me:9104/trainers',
    params = {'trainer_id' : 3383})
    assert response.json()['trainer_name'] == 'Хоша'