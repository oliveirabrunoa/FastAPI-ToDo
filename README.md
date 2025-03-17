# TaskManager

Este repositório contém materiais e exemplos de código para o estudo do FastAPI. Uma aplicação de gestão de tarefas através de operações de CRUD.

## Conteúdo

- Introdução ao FastAPI
- Configuração do ambiente
- Recursos adicionais

## Introdução ao FastAPI

FastAPI é um framework moderno, rápido (alta performance), para construção de APIs com Python 3.6+ baseado em padrões como OpenAPI e JSON Schema.

## Configuração do Ambiente

Para configurar o ambiente de desenvolvimento, siga os passos abaixo:

1. Clone o repositório:
    ```bash
    git clone https://github.com/SeuUsuario/Estudos-FastAPI.git
    ```
2. Crie um ambiente virtual:
    ```bash
    python -m venv venv
    ```
3. Ative o ambiente virtual:
    - No Windows:
        ```bash
        .\venv\Scripts\activate
        ```
    - No Linux/MacOS:
        ```bash
        source venv/bin/activate
        ```
4. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

## Criando bando de dados
```
python create_db.py
 ```
 

## Executando o projeto
```
uvicorn main:app --reload
 ```
## Endpoints

### Obter todas as tarefas
- **URL:** `/tasks`
- **Método:** `GET`
- **Resposta:** Lista de tarefas

### Obter uma tarefa
- **URL:** `/tasks/{task_id}`
- **Método:** `GET`
- **Resposta:** Detalhes da tarefa

### Criar uma nova tarefa
- **URL:** `/tasks`
- **Método:** `POST`
- **Corpo da Requisição:** 
- **Resposta:** Detalhes da tarefa criada

### Atualizar uma tarefa
- **URL:** `/tasks/{task_id}`
- **Método:** `PUT`
- **Corpo da Requisição:** 
- **Resposta:** Detalhes da tarefa atualizada

### Excluir uma tarefa
- **URL:** `/tasks/{task_id}`
- **Método:** `DELETE`
- **Resposta:** Mensagem de sucesso

## Licença
Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

## Recursos Adicionais

- [Documentação Oficial do FastAPI](https://fastapi.tiangolo.com/)
- [Repositório no GitHub](https://github.com/tiangolo/fastapi)
- [Tutoriais e Artigos](https://fastapi.tiangolo.com/tutorial/)
