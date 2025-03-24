# Caso de Teste: CRUD de Especialidade

## Objetivo
Verificar se as operações de criação, listagem, busca por nome e deleção de uma especialidade funcionam corretamente no endpoint `/especialidade`.

## Pré-condições
1. A API deve estar em execução no endereço: `http://localhost:3000`.
2. O banco de dados (ou armazenamento equivalente) deve estar configurado e acessível.
3. O endpoint `/especialidade` deve aceitar requisições HTTP nos métodos **POST**, **GET** e **DELETE**.

## Procedimento de Teste

1. **Criação (POST /especialidade)**
   - Enviar uma requisição POST com o seguinte corpo:
     ```json
     {
       "nome": "Teste"
     }
     ```
   - Verificar se o **status code** é `201` e se a resposta retorna os dados da especialidade criada.

2. **Listagem (GET /especialidade)**
   - Enviar uma requisição GET para `/especialidade`.
   - Verificar se o **status code** é `200` e se a lista de especialidades inclui a recém-criada `"Teste"`.

3. **Busca por Nome (GET /especialidade/Teste)**
   - Enviar uma requisição GET para `/especialidade/Teste`.
   - Verificar se o **status code** é `200` e se os dados retornados correspondem à especialidade `"Teste"`.

4. **Deleção (DELETE /especialidade/Teste)**
   - Enviar uma requisição DELETE para `/especialidade/Teste`.
   - Verificar se o **status code** é `200` e se a resposta indica que a especialidade foi removida.

5. **Verificação Pós-deleção**
   - Enviar novamente uma requisição GET para `/especialidade/Teste`.
   - Verificar se o **status code** é `404`, confirmando que a especialidade não está mais disponível.

## Resultado Esperado
- **Criação:** Retorno `201` com os dados da nova especialidade.
- **Listagem:** Retorno `200` com uma lista que contenha a especialidade `"Teste"`.
- **Busca por Nome:** Retorno `200` com os dados corretos da especialidade `"Teste"`.
- **Deleção:** Retorno `200` indicando sucesso na deleção.
- **Pós-deleção:** Retorno `404` para a busca de `"Teste"`, confirmando que foi removida.

## Resultado Obtido

Após a execução dos testes automatizados, os seguintes resultados foram observados:

1. **Criação (POST /especialidade):**
   - **Status Code:** 201
   - **Resposta:**
     ```json
     {
       "id": 1,
       "nome": "Teste"
     }
     ```

2. **Listagem (GET /especialidade):**
   - **Status Code:** 200
   - **Resposta:**
     ```json
     [
       {
         "id": 1,
         "nome": "Teste"
       }
     ]
     ```

3. **Busca por Nome (GET /especialidade/Teste):**
   - **Status Code:** 200
   - **Resposta:**
     ```json
     {
       "id": 1,
       "nome": "Teste"
     }
     ```

4. **Deleção (DELETE /especialidade/Teste):**
   - **Status Code:** 200
   - **Resposta:**
     ```json
     {
       "message": "Especialidade deletada"
     }
     ```

5. **Verificação Pós-deleção (GET /especialidade/Teste):**
   - **Status Code:** 404
   - **Resposta:**
     ```json
     {
       "error": "Especialidade não encontrada"
     }
     ```
