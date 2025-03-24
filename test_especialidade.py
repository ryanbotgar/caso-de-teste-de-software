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

def test_delete():
    print("\nTeste: Deletar Especialidade (DELETE /especialidade/Teste)")
    response = requests.delete(f"{BASE_URL}/Teste")
    print("Status:", response.status_code)
    print("Resposta:", response.json())
    return response.status_code == 200

def main():
    # Executa o teste de criação
    if test_create():
        print("Criação realizada com sucesso!")
    else:
        print("Falha na criação da especialidade!")
    
    # Executa o teste de listagem
    if test_list():
        print("Listagem realizada com sucesso!")
    else:
        print("Falha na listagem!")
    
    # Executa o teste de busca por nome
    if test_get_by_name():
        print("Busca realizada com sucesso!")
    else:
        print("Falha na busca pela especialidade!")
    
    # Executa o teste de deleção
    if test_delete():
        print("Deleção realizada com sucesso!")
    else:
        print("Falha ao deletar a especialidade!")
    
    # Verificação pós-deleção: a especialidade "Teste" não deve existir
    print("\nTeste: Verificar que a especialidade foi deletada (GET /especialidade/Teste)")
    response = requests.get(f"{BASE_URL}/Teste")
    print("Status (esperado 404):", response.status_code)
    print("Resposta:", response.json())

if __name__ == '__main__':
    main()


