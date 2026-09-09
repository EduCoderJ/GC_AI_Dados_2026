
# Resolução de Exercícios — Aula 05

Repositório destinado à entrega dos desafios de Excel e controle de versão.

---

### 1. Ex.excel01 — Tabela de Produtos da Cafeteria
* Preenchimento dos dados do cardápio e formatação da coluna `Valor_Unitario` para Moeda (`R$`).

---

### 2. Ex.excel02 — Falidos e Quebrados LTDA (=SE)
* Classificação das vendas por funcionário via lógica `=SE()` aninhada:
  * Vendas > 5 → `"Ótimo"`
  * Vendas = 5 → `"Regular"`
  * Vendas < 5 → `"Pessimo"`
* **Fórmula (célula D3):** `=SE(C3>5; "Ótimo"; SE(C3=5; "Regular"; "Pessimo"))`

---

### 3. Ex.excel03 — Notas Escolares (Média, =SE e Formatação)
* Média trimestral calculada via `=MÉDIA(C3:E3)`.
* Resultado via `=SE(F3>=6; "Aprovado"; "Reprovado")`.
* **Formatação Condicional:**
  * Valores < 6.0 em vermelho / Valores >= 6.0 em verde.
  * Células com `"Aprovado"` em verde e `"Reprovado"` em vermelho.

---

### 4. Ex.excel04 — Recrutamento para Vaga de Emprego (=E, =OU)
* Triagem de candidatos com múltiplos requisitos simultâneos (Idade >= 18, Ensino Médio, Curso e Exp >= 3 anos).
* **Fórmula (célula F3):** `=SE(E(B3>=18; C3="Sim"; D3="Sim"; E3>=3); "Apto"; "Não Apto")`
* **Formatação Condicional:** Destaque em verde para `"Apto"` e vermelho para `"Não Apto"`.
