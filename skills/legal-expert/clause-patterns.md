# Clause Patterns - Common Clauses in Civil Contracts

## Structural Patterns

### Pattern 1: Partes e Definições

**Essencial (Always Include):**
```
PARTES:
- [Nome Completo] (doravante "Contratante")
- [Nome Completo] (doravante "Contratado")

DEFINIÇÕES:
- "Serviço(s)" significa [descrição específica]
- "Período" significa [data inicial] até [data final]
- "Valores" significa [moeda] [valores específicos]
```

**Red Flags:**
- Partes não identificadas claramente
- Persona jurídica confusa (PJ vs PF)
- Definições vagas ou faltantes
- Referência a "apêndices" não inclusos

---

### Pattern 2: Objeto & Escopo

**Well-Written Example:**
```
2. DO OBJETO
2.1 O objeto deste contrato é a prestação de [SERVIÇO ESPECÍFICO] 
    conforme detalhado no ANEXO A.
2.2 Exclui-se expressamente: [Listar o que NÃO está incluído]
2.3 A execução ocorrerá em [LOCAL/FORMATO] conforme cronograma 
    do ANEXO B.
```

**Problems to Watch:**
- Escopo vago: "Consultoria geral em TI"
- Sem exclusões explícitas
- Sem cronograma ou deliverables
- Mudanças de escopo permitidas sem acordo

---

### Pattern 3: Vigência & Prazo

**Well-Written:**
```
3. VIGÊNCIA
3.1 Este contrato tem vigência de [X] meses, iniciando-se em 
    [DD/MM/AAAA] e terminando em [DD/MM/AAAA].
3.2 Renova-se automaticamente por períodos iguais, a menos que 
    uma parte notifique rescisão com [30] dias de antecedência.
3.3 Notificação deve ser feita por escrito (e-mail + carta registrada).
```

**Red Flags:**
- Sem data de término (contrato indefinido)
- Renovação automática sem cláusula de saída
- Requisitos de notificação vagos
- Prazos para aviso insuficientes

---

### Pattern 4: Remuneração & Pagamento

**Safe Structure:**
```
4. REMUNERAÇÃO
4.1 Contratante pagará R$ [VALOR] conforme:
    - R$ [X] no início (ANEXO C)
    - R$ [Y] mensal, vencido em [dia 10] de cada mês
    - R$ [Z] ao término do Serviço

4.2 Forma de pagamento: [transferência, boleto, outro]
4.3 Juros de mora: [X]% a.m. após 15 dias de atraso
4.4 Reajuste anual: [IPCA] ou [percentual fixo]%
```

**Danger Zones:**
- Valor "a combinar"
- Sem datas de pagamento claras
- Juros/multa excessivos (acima de 2% + Selic)
- Sem cláusula de reajuste (erosão inflacionária)
- Retenção de pagamento sem justificativa legal

---

### Pattern 5: Obrigações das Partes

**Best Practice (Bilateral & Specific):**
```
5. OBRIGAÇÕES
5.1 DO CONTRATADO:
    a) Executar o Serviço com padrão profissional
    b) Entregar resultado até [DATA]
    c) Fornecer relatórios mensais
    d) Manter confidencialidade (vide cláusula X)

5.2 DO CONTRATANTE:
    a) Fornecer recursos/acesso necessários
    b) Realizar pagamentos conforme cronograma
    c) Fornecer feedback em prazo razoável [X dias]
```

**Anti-Patterns:**
- Obrigações unilaterais (só uma parte tem deveres)
- Obrigações vagas: "fazer o melhor"
- Sem critério de aceitação
- Sem prazos para cumprimento

---

### Pattern 6: Responsabilidade & Indenização

**Balanced Approach:**
```
6. RESPONSABILIDADE
6.1 Cada parte será responsável por:
    - Danos diretos causados por seus atos/omissões
    - Quebra de confidencialidade
    - Violação de direitos de terceiros

6.2 Excludem-se de responsabilidade:
    - Danos indiretos, incidentais, consequenciais
    - Lucro cessante além de [X]
    - Danos por culpa exclusiva da outra parte

6.3 Limite total de indenização: [R$ X] ou [Y]% do valor total
```

**Red Flags:**
- Responsabilidade 100% em uma parte
- Sem limite de indenização
- Responsabilidade por danos "de qualquer natureza"
- Cláusula exonera completamente uma parte

---

### Pattern 7: Confidencialidade

**Standard Protection:**
```
7. CONFIDENCIALIDADE
7.1 Informações confidenciais sao aquelas marcadas como 
    [CONFIDENCIAL] ou claramente sensiveis de negócio.

7.2 Receptor se compromete a:
    - Não divulgar a terceiros (exceto advogados/contadores)
    - Manter separado de conhecimento público
    - Retornar/destruir ao término do contrato

7.3 Exceções: informações públicas, já conhecidas, 
    ou obtidas legitimamente de terceiros.

7.4 Duração: [2-5] anos após término do contrato
```

**Common Issues:**
- Confidencialidade sem prazo final
- Sem exceções claras (público, conhecimento prévio)
- Muito abrangente (inclui o óbvio)
- Sem mecanismo de descoberta em litígio

---

### Pattern 8: Propriedade Intelectual

**Clear Allocation:**
```
8. PROPRIEDADE INTELECTUAL
8.1 Materiais pré-existentes do Contratado mantêm propriedade 
    com o Contratado. Contratante recebe licença de uso.

8.2 Trabalhos derivados/customizados criados durante vigência 
    pertencem a [Contratante/Contratado/Compartilhado].

8.3 Contratado retém direito de:
    - Usar métodos/processos desenvolvidos em futuros projetos
    - Listar como case study (sem dados específicos)

8.4 Contratante recebe licença perpétua de uso do resultado final.
```

**Danger:**
- Sem clareza sobre propriedade
- "Todos direitos pertencem ao contratante" (muito amplo)
- Sem licença de uso garantida
- Contratado não pode reaproveitar trabalho

---

### Pattern 9: Término & Rescisão

**Structured Exit:**
```
9. TÉRMINO
9.1 Rescisão por conveniência: 
    - Qualquer parte pode rescindir com [60] dias de aviso
    - Contratante paga por trabalho realizado até data

9.2 Rescisão por causa/inadimplemento:
    - Notificar falha por escrito
    - 15 dias para remediar
    - Se não remediar, rescindir sem aviso adicional

9.3 Obrigações ao término:
    - Retorno de materiais
    - Cessação de confidencialidade após [X] dias
    - Assist na transição: [X horas] sem custo
```

**Problems:**
- Rescisão unilateral sem prazo
- Sem indenização ao término
- Obrigações pós-término indefinidas
- Sem período de transição/knowledge transfer

---

### Pattern 10: Litígio & Lei Aplicável

**International/Safe Standard:**
```
10. LEI E FORO
10.1 Este contrato é regido pelas leis da República Federativa 
     do Brasil, especificamente [estado].

10.2 Resolução de Disputas:
     a) Negociação de boa-fé: [30] dias
     b) Mediação: [60] dias
     c) Arbitragem (UNCITRAL) ou Litígio (Tribunal de [Foro])

10.3 Prevalecem disposições que favoreçam a parte prejudicada.
```

**Caution:**
- Jurisdição distante (caro para litigar)
- Lei estrangeira em mercado brasileiro
- Sem tentativa de resolução alternativa
- One-sided dispute resolution

---

## Red Flags by Clause Type

### Geral

| Flag | Significado | Ação |
|------|-------------|------|
| "Conforme necessário" | Escopo aberto | Definir limites |
| "Padrão da indústria" | Vago, não busca específica | Pedir exemplo/documentação |
| "A nosso critério" | Poder unilateral | Adicionar objetividade/mediação |
| "Sem exceção" | Muito restritivo | Negociar razoabilidade |
| Frase repetida 5x | Redundância/ênfase artificial | Simplificar, pode indicar desespero |

---

## Protective Clauses (Adicione ao Seu Contrato)

### 1. Amendment & Modification
```
Nenhuma alteração é válida a menos que por escrito assinada 
por ambas as partes.
```

### 2. Severability
```
Se qualquer cláusula for inválida, as demais permanecem em vigor.
```

### 3. Waiver
```
Falha em exercer direito não constitui renúncia desse direito.
```

### 4. Entire Agreement
```
Este contrato contém todo o acordo entre as partes e supersede 
conversas prévias/e-mails.
```

### 5. Attorney Fees
```
Parte vencedora em litígio recupera honorários advocatícios 
e custas processuais.
```
