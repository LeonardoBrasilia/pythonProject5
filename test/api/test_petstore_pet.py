import requests
import pytest

base_url = 'https://petstore.swagger.io/v2/pet'
headers = {'Content-Type': 'application/json'}


def testar_incluir_pet():
    # Configura
    # Dados de entrada vêm do pet'.json
    status_code_esperado = 200
    nome_pet_esperado = 'Snoopy'
    tag_esperada = 'vacinado'

    # Executa
    resposta = requests.post(
        url=base_url,
        data=open('E:/Users/Léo/PycharmProjects/pythonProject5/test/api/test_petstore_pet.py', 'rb'),
        headers=headers
    )

    # Formata
    print(resposta)
    print(resposta.status_code)
    corpo_da_resposta = resposta.json()
    print(corpo_da_resposta)

    # Valida
    assert resposta.status_code == status_code_esperado
    assert corpo_da_resposta['name'] == nome_pet_esperado
    # assert corpo_da_resposta['tags.name'] == tag_esperada
