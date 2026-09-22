# Atividade 3: Estratégia e Projeto de Testes do LocalEats

> Substituam os campos entre colchetes pelas respostas da equipe e removam as instruções antes da entrega.

## 1. Identificação

**Turma:** ADS 5º semestre noite    
**Data:** 21/09/2026

### Integrantes

| Nome | Usuário no GitHub |
|---|---|
| Felipe Rosso | @DevRossO |

**Elemento de Competência:** Planejar e projetar testes selecionando técnicas adequadas.

**Aplicação:** <https://local-eats-unisenac.vercel.app/>

---

## 2. Tarefa 1: Planejamento dos testes

### 2.1 Objetivo dos testes

Verificar se o fluxo de montagem e finalização de pedidos no LocalEats valida corretamente as quantidades de itens, impede a criação de pedidos vazios e lida de forma adequada com múltiplos pratos.

### 2.2 Escopo

#### Funcionalidades incluídas

| Integrante | Funcionalidade incluída | O que será verificado |
|---|---|---|
| Felipe Rosso | Fazer Pedido | Seleção de pratos no cardápio, limites de quantidade permitida de itens e geração do pedido no sistema. |

> Acrescentem ou removam linhas conforme o número de integrantes.

#### Funcionalidade não incluída

| Funcionalidade não incluída | Justificativa |
|---|---|
| Criar conta e Autenticação | Não faz parte do escopo direto de regras do carrinho e finalização de compras escolhido para este planejamento. |

### 2.3 Abordagem

| Item | Decisão da equipe | Justificativa |
|---|---|---|
| Níveis de teste | Sistema | O fluxo de pedido será analisado de ponta a ponta pela interface gráfica de usuário (UI). |
| Tipos de teste | Funcional | O objetivo é validar as regras de negócio de adição de itens e emissão do pedido. |
| Perspectiva caixa-preta ou caixa-branca | Caixa-preta | As validações focarão nas entradas (botões e quantidades) e saídas esperadas, sem acesso ao código-fonte. |
| Técnicas de teste | Análise de Valor Limite e Tabela de Decisão | Permitirão testar os limites numéricos de itens por prato e as combinações de condições para concluir o pedido. |

### 2.4 Ambiente e responsabilidades

| Item | Definição |
|---|---|
| Ambiente necessário | URL: https://local-eats-unisenac.vercel.app/ 
Navegador: Google Chrome / Mozilla Firefox (Desktop) Dispositivo: PC/Notebook Contas/Dados: Usuário autenticado na plataforma e restaurante com cardápio ativo.|
| Responsáveis pelo planejamento | Felipe Rosso |
| Responsáveis pela especificação dos casos | Felipe Rosso |
| Responsáveis pela futura execução | Felipe Rosso |

### 2.5 Critérios

| Critério | Definição da equipe |
|---|---|
| Entrada | LocalEats acessível via web, usuário logado no sistema e restaurantes cadastrados com itens no cardápio. |
| Saída | Todos os 3 casos de teste planejados executados e com seus resultados registrados no relatório. |
| Suspensão | Queda da aplicação (sistema fora do ar/erro HTTP 500) ou impossibilidade de adicionar itens ao cardápio. |

---

## 3. Tarefa 2: Riscos e técnicas de teste

### 3.1 Análise dos riscos

> Cada integrante deve analisar pelo menos um risco relacionado à funcionalidade escolhida. No trabalho individual, devem ser analisados dois riscos.

| ID | Integrante | Funcionalidade | Risco | Consequência | Probabilidade | Impacto | Prioridade | Justificativa |
|---|---|---|---|---|:---:|:---:|:---:|---|
| R01 | Felipe Rosso | Fazer pedido | O sistema permitir a inclusão de quantidade nula (0) ou negativa de pratos no pedido. | O usuário gera um pedido sem itens ou corrompe o valor total da compra na base de dados. | Média | Alto | Alta | Pedidos sem itens geram falhas no backend e problemas operacionais com o restaurante. |
| R02 | Felipe Rosso | Fazer pedido | Falha na associação de múltiplos pratos a um mesmo número de pedido (criação de IDs separados por item). | O cliente e o restaurante recebem múltiplos pedidos fragmentados para uma única compra, dobrando taxas ou gerando confusão na entrega. | Alta | Médio | Alta | Comportamento identificado em testes exploratórios que afeta a experiência do usuário e o fluxo de checkout. |

> Acrescentem as linhas necessárias e mantenham identificadores únicos: R01, R02, R03 etc.

### 3.2 Aplicação das técnicas

> Cada integrante deve aplicar pelo menos uma técnica adequada à funcionalidade e ao risco analisado. A equipe deve utilizar, no conjunto da atividade, pelo menos duas técnicas diferentes.

#### Análise do integrante 1

**Integrante:** Felipe Rosso  
**Funcionalidade:** Fazer pedido  
**Risco relacionado:** R01  
**Técnica escolhida:** Análise de valor limite

**Por que a técnica foi escolhida:**  
A quantidade de itens adicionados a um pedido possui limites fronteiriços (mínimo de 1 item e limite máximo operacional do sistema). A Análise de Valor Limite é ideal para testar justamente as fronteiras do que é aceito e rejeitado.

**Aplicação da técnica:**  
Regra: A quantidade de um prato individual no pedido deve ser entre 1 e 99 unidades.

**Fronteira Inferior: 0 (Inválido), 1 (Válido), 2 (Válido)

**Fronteira Superior: 98 (Válido), 99 (Válido), 100 (Inválido)

**Casos derivados:** 

**CT01: Tentar adicionar 0 unidades de um prato ao pedido.

**CT02: Adicionar 1 unidade de um prato ao pedido (limite mínimo válido).

#### Análise do integrante 2

**Integrante:** Felipe Rosso 
**Funcionalidade:** Fazer pedido  
**Risco relacionado:** R02  
**Técnica escolhida:** Tabela de decisão

**Por que a técnica foi escolhida:**  
A finalização do pedido depende da combinação entre a quantidade de itens no carrinho e se esses itens pertencem ao mesmo restaurante ou a estabelecimentos diferentes.

**Aplicação da técnica:**

| Regra | Possui itens no carrinho? | Itens são do mesmo restaurante? | Resultado Esperado |
| :--- | :--- | :--- | :--- |
| **1** | Não | N/A | Bloquear o botão de finalizar pedido. |
| **2** | Sim | Sim | Consolidar todos os pratos em um **único ID de pedido**. |
| **3** | Sim | Não | Emitir alerta ou separar pedidos por estabelecimento conforme regra de negócio. |

**Casos derivados:**
CT03: Finalizar pedido contendo dois pratos diferentes do mesmo restaurante.

> Repitam ou removam a seção de análise conforme o número de integrantes.

---

## 4. Tarefa 3: Casos de teste e rastreabilidade

### 4.1 Casos de teste

> No trabalho individual, elabore três casos. No trabalho em equipe, cada integrante deve elaborar pelo menos dois casos relacionados à própria funcionalidade.

### CT01: Bloquear adição de quantidade zero (0) de itens

**Integrante responsável:** Felipe Rosso  
**Funcionalidade:** Fazer pedido  
**Risco ou requisito relacionado:** R01  
**Técnica utilizada:** Análise de Valor Limite

**Pré-condição:**  
Usuário autenticado e na página de detalhes do restaurante "Restaurante Sabor 0".

**Dados de entrada:**  
Prato "Prato Especial 0", Quantidade: 0

**Passos:**

1. Acessar a página do "Restaurante Sabor 0".
2. Localizar o item "Prato Especial 0".
3. Definir o campo de quantidade com o valor 0.

**Resultado esperado:**  
[Comportamento observável que indicará que o teste passou.]

---

### CT02: Adicionar a quantidade mínima válida (1 unidade) ao pedido

**Integrante responsável:** Felipe Rosso  
**Funcionalidade:** Fazer pedido 
**Risco ou requisito relacionado:** R01  
**Técnica utilizada:** Análise de valor limite

**Pré-condição:**  
Usuário autenticado com o carrinho de compras vazio.

**Dados de entrada:**  
Prato "Prato Especial 0", Quantidade: 1, Valor unitário: R$ 59,17

**Passos:**

1. Navegar até o cardápio do restaurante.
2. Selecionar o "Prato Especial 0".
3. Garantir a quantidade 1 e clicar no botão "+ Adicionar".
4. Acessar a tela/resumo do pedido/carrinho.

**Resultado esperado:**  
O prato é adicionado com sucesso ao pedido, apresentando a quantidade 1 e o valor total atualizado corretamente para R$ 59,17.

---

### CT03: Consolidar múltiplos pratos do mesmo restaurante em um único pedido

**Integrante responsável:** Felipe Rosso  
**Funcionalidade:** Fazer pedido 
**Risco ou requisito relacionado:** R02  
**Técnica utilizada:** Tabela de decisão

**Pré-condição:**  
Usuário autenticado na plataforma LocalEats

**Dados de entrada:**  
**Prato 1: "Prato Especial 0" (R$ 59,17)

**Prato 2: "Prato Especial 1" (R$ 46,81)

**Passos:**

1. Acessar o "Restaurante Sabor 0".
2. Clicar em "+ Adicionar" no "Prato Especial 0".
3. Clicar em "+ Adicionar" no "Prato Especial 1".
4. Ir para a tela de confirmação/fechamento de pedido.
5. Clicar em "Finalizar Pedido".
6. Navegar para a página "Meus Pedidos".

**Resultado esperado:**  
O sistema registra apenas 1 número de pedido (ID) contendo os dois pratos em seu detalhamento, com o valor total somado de R$ 105,98.

---


> Copiem o modelo acima e continuem a numeração para criar os demais casos: CT03, CT04, CT05 etc.

### 4.2 Matriz de rastreabilidade

### 3.2 Matriz de rastreabilidade

| Integrante | Funcionalidade | Risco ou requisito | Técnica utilizada | Casos de teste |
| :--- | :--- | :--- | :--- | :--- |
| Felipe Rosso | Fazer pedido | **R01:** Permissão de quantidade zerada/inválida no pedido. | Análise de Valor Limite | CT01, CT02 |
| Felipe Rosso | Fazer pedido | **R02:** Fragmentação de pedido ao incluir múltiplos pratos. | Tabela de Decisão | CT03 |

> Acrescentem as linhas necessárias. Verifiquem se todos os riscos selecionados possuem casos de teste relacionados.

---

## 5. Uso de inteligência artificial

**Ferramenta utilizada:**  
Gemini

**Como foi utilizada:**  
Apoio no planejamento dos casos de teste, definição da Análise de Valor Limite/Tabela de Decisão e estruturação do plano de testes em formato Markdown.

**Uma sugestão que precisou ser alterada ou rejeitada:**  
A IA originalmente sugeriu um risco focado em falha na integração de gateways de pagamento (Cartão de Crédito/PIX). A sugestão foi alterada/rejeitada porque o LocalEats na versão testada possui apenas um fluxo simples de simulação de pedido, sem checkout com gateway real de pagamentos.

**Como as respostas foram verificadas:**  
A matriz de rastreabilidade e a aplicação das técnicas foram revisadas manualmente.