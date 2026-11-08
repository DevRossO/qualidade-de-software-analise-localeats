# Atividade 4: Testes Automatizados do LocalEats

## 1. Identificação

| Integrante | Turma | Projeto |
|---|---|---|
| Felipe Rosso | ADS - 5º semestre noite | LocalEats |

Aplicação testada: <https://local-eats-unisenac.vercel.app/>

Realizei o trabalho sozinho. A regra escolhida foi a validação da
quantidade de itens e o fluxo funcional escolhido foi abrir o cadastro na tela inicial.

## 2. Regra implementada

A função `quantidade_itens_valida(quantidade)` retorna `True` para quantidades
entre 1 e 10, e `False` para zero ou quantidades acima de 10.
Quantidades negativas geram `ValueError`.

Arquivo: `src/regras_localeats.py`

## 3. Testes unitários

Os testes estão em `tests/test_regras_localeats.py` e foram escritos com pytest:

- `test_quantidade_de_itens_dentro_do_limite_e_valida`: verifica um valor válido.
- `test_quantidade_acima_do_limite_nao_e_valida`: verifica uma quantidade acima do limite.

### TDD de Felipe Rosso

**Regra escolhida:** validar quantidade de itens entre 1 e 10.

**Primeiro teste escrito:** verificar que a quantidade 3 retorna `True`.

**Por que o teste falhou inicialmente:** a função ainda não existia no início do
desenvolvimento orientado a testes.

**Implementação mínima realizada:** foi criada a função com a comparação do
intervalo válido.

**Segundo teste escrito:** verificar que a quantidade 11 retorna `False`.

**Melhoria ou refatoração realizada:** foi incluida a validação de quantidade
negativa com `ValueError`, mantendo a função curta e direta.

### Explicação individual

O teste de quantidade acima do limite usa o valor 11 porque 10 ainda é aceito
pela regra. A assertion confirma que a função não permite uma quantidade maior
que o limite operacional definido.

## 4. Teste funcional com Playwright

O teste `tests/test_localeats.py::test_abrir_formulario_de_cadastro_no_localeats`
acessa a página inicial e clica em `Criar Conta`.

As duas assertions verificam que:

1. o formulário de cadastro fica visível;
2. o campo de nome do cadastro fica visível.

O teste usa locators do Playwright e não utiliza `time.sleep`.

## 5. Identificação das responsabilidades

| ID | Integrante | Tipo | Comportamento verificado | Arquivo e função |
|---|---|---|---|---|
| TU01 | Felipe Rosso | Unitário | Quantidade válida entre 1 e 10 | `tests/test_regras_localeats.py::test_quantidade_de_itens_dentro_do_limite_e_valida` |
| TU02 | Felipe Rosso | Unitário | Quantidade acima de 10 | `tests/test_regras_localeats.py::test_quantidade_acima_do_limite_nao_e_valida` |
| TF01 | Felipe Rosso | Funcional | Abrir cadastro na página inicial do LocalEats | `tests/test_localeats.py::test_abrir_formulario_de_cadastro_no_localeats` |

## 6. Execução

Os testes devem ser executados dentro desta pasta com:

```powershell
python -m pytest -v
```

O resultado da execução está registrado em `relatorio-pytest.txt`.

## 7. Uso de inteligência artificial

**Ferramenta utilizada:** Copilot no VS Code.

**Como a ferramenta foi utilizada:** apoio na criação da estrutura de testes,
na implementação da regra simples e na organização deste relatório.

**Uma sugestão que precisou ser alterada ou rejeitada:** foram mantidos somente
dois testes unitários e um teste funcional, pois esta é a quantidade mínima para
um trabalho individual.

**Como o código sugerido foi verificado:** a estrutura foi comparada com o
enunciado, os locators foram conferidos no HTML da aplicação e os testes foram
executados com pytest.
