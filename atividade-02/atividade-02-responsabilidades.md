# Atividade 2: Organização da Qualidade no LocalEats

> Substituam os campos entre colchetes pelas respostas da equipe e removam as instruções antes da entrega.

## 1. Identificação

**Turma:** ADS 5º semestre noite    
**Data:** 16/09/2026

### Integrantes

| Nome | Usuário no GitHub |
|---|---|
| Felipe Rosso | @DevRossO |


**Elemento de Competência:** Identificar papéis, responsabilidades e competências relacionadas às atividades de qualidade e testes.

---

## 2. Tarefa 1: Diagnóstico da situação

### 2.1 Problemas organizacionais

| Problema identificado | Possível consequência para o produto ou para a equipe |
|---|---|
| As funcionalidades são entregues sem regras claras do que é considerado "pronto" | Funcionalidades chegam em produção com defeitos graves e comportamentos inesperados, gerando retrabalho constante |
| Cultura de qualidade centralizada exclusivamente no QA: Acreditar que apenas o QA é responsável por testar o software | Gargalo no desenvolvimento, atraso nas entregas e baixa adesão a testes unitários/automatizados pelos desenvolvedores. |
| Ausência de processo formal para gestão de defeitos e deploy | Bugs são esquecidos ou ignorados no backlog, e liberações em produção ocorrem de forma instável sem validação final |

### 2.2 Responsabilidade pela qualidade

**A qualidade do LocalEats deve ser responsabilidade exclusiva do profissional de QA? Justifiquem.**

Não. Em metodologias ágeis, a qualidade é uma responsabilidade compartilhada por toda a equipe. O PO garante requisitos claros, os Desenvolvedores constroem código testável e sem bugs funcionais, o QA atua como facilitador e estrategista de testes. A qualidade faz parte do processo, não adicionada no final.

---

## 3. Tarefa 2: Papéis e competências

> Cada integrante deve ser responsável pela análise de pelo menos um papel. Acrescentem ou removam linhas conforme a composição da equipe e os papéis escolhidos.

| Integrante | Papel analisado | Responsabilidades relacionadas à qualidade | Competências técnicas | Competências comportamentais |
|---|---|---|---|---|
| Felipe Rosso | Desenvolver(Dev) | Escrever código limpo, criar testes unitários/integrados, realizar code reviews e corrigir defeitos apontado | Git, Clean Code, Testes Unitários | Atenção aos detalhes, postura colaborativa, aceitação de feedback e orientação a soluções |

---

## 4. Tarefa 3: Matriz de responsabilidades

> Substituam “Papel 1”, “Papel 2”, “Papel 3” e “Papel 4” pelos papéis definidos pela equipe. Acrescentem ou removam colunas conforme necessário.

Utilizem:

- **R:** responsável por executar a atividade;
- **A:** aprovador ou responsável final;
- **C:** consultado antes da execução ou decisão;
- **I:** informado sobre o resultado.

| Atividade de qualidade | PO | Dev | QA | DevOps |
|---|:---:|:---:|:---:|:---:|
| Definir critérios de aceitação | **A** | C | C | I |
| Revisar requisitos | **A** | C | C | I |
| Implementar a funcionalidade | I | **R** | C | I |
| Revisar o código | I | **R / A** | C | I |
| Criar testes unitários | I | **R / A** | C | I |
| Planejar e executar testes do sistema | I | C | **R / A** | I |
| Registrar e acompanhar defeitos | I | C | **R / A** | I |
| Priorizar a correção dos defeitos | **A** | C | **R** | I |
| Aprovar a disponibilização da versão | **A** | C | C | **R** |

### 4.1 Lacuna ou conflito encontrado

**Lacuna ou conflito:**  
**Falta de clareza sobre quem autoriza a liberação do sistema para os usuários (Aprovar a disponibilização da versão).** Antes de organizar os papéis, qualquer desenvolvedor podia colocar o código no ar assim que terminava de programar, sem passar por uma validação final do PO ou por um teste completo do QA.

**Consequência:**  
Risco alto de lançar versões do LocalEats com defeitos visíveis para os clientes, prejudicando a imagem do produto e gerando correria na equipe para arrumar às pressas.

### 4.2 Práticas de QA recomendadas

| Prática recomendada | Problema que ajuda a resolver | Papéis envolvidos |
|---|---|---|
| Estabelecer regras claras para quando uma tarefa pode ser iniciada (DoR) e quando está pronta para ir a produção (DoD) | Funcionalidades incompletas ou sem testes subindo para produção. | PO, Desenvolvedor e QA |
| Incluir o QA e Devs na discussão dos requisitos e critérios de aceitação antes de escrever o código. | Falhas conceituais de requisitos identificadas tarde demais na esteira. | PO, Desenvolvedor e QA |

---

## 5. Uso de inteligência artificial

**Ferramenta utilizada:**  
Gemini

**Como foi utilizada:**  
Auxilio na formulação das justificativas teóricas de qualidade de software

**Como as respostas foram verificadas:**  
