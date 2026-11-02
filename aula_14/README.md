# API Casa de Suco 🧃

Aplicação desenvolvida em Python com **FastAPI** para gerenciar receitas de sucos e calcular automaticamente os valores nutricionais (calorias e açúcar) através da integração com a API pública **Fruityvice**.

## Endpoints Disponíveis
- `GET /frutas/{nome}`: Consulta calorias e açúcar de uma fruta específica na API externa.
- `POST /sucos`: Cadastra um novo suco informando nome, lista de frutas e sabor, calculando os totais com base em 100g por fruta.
- `GET /sucos`: Retorna a lista de todos os sucos cadastrados.
- `PUT /sucos/{id}`: Atualiza os dados de um suco e recalcula os valores nutricionais (Desafio Bônus).

## Como Executar Localmente

1. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   # No Windows: venv\Scripts\activate
   # No Linux/Mac: source venv/bin/activate