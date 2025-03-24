import requests

# URL base da API para "especialidade"
BASE_URL = 'http://localhost:3000/especialidade'

def test_create():
    print("Teste: Criar Especialidade (POST /especialidade)")
    payload = {"nome": "Teste"}
    response = requests.post(BASE_URL, json=payload)
    print("Status:", response.status_code)
    print("Resposta:", response.json())
    return response.status_code == 201

def test_list():
    print("\nTeste: Listar Especialidades (GET /especialidade)")
    response = requests.get(BASE_URL)
    print("Status:", response.status_code)
    print("Resposta:", response.json())
    return response.status_code == 200

def test_get_by_name():
    print("\nTeste: Buscar Especialidade (GET /especialidade/Teste)")
    response = requests.get(f"{BASE_URL}/Teste")
    print("Status:", response.status_code)
    print("Resposta:", response.json())
    return response.status_code == 200


