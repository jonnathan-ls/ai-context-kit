# Ferramentas do Agente

## Visão Geral

Este documento lista as ferramentas disponíveis para o agente.

## Ferramentas Principais

### Tool 1: [Nome da Ferramenta]

**Descrição**: O que esta ferramenta faz.

**Parâmetros**:
- `param1` (string, obrigatório): Descrição
- `param2` (number, opcional): Descrição

**Retorno**: Descrição do que a ferramenta retorna.

**Exemplo de Uso**:
```json
{
  "tool": "tool1",
  "parameters": {
    "param1": "valor"
  }
}
```

---

### Tool 2: [Nome da Ferramenta]

**Descrição**: O que esta ferramenta faz.

**Parâmetros**:
- `param1` (string, obrigatório): Descrição
- `param2` (boolean, opcional): Descrição

**Retorno**: Descrição do que a ferramenta retorna.

**Exemplo de Uso**:
```json
{
  "tool": "tool2",
  "parameters": {
    "param1": "valor"
  }
}
```

---

### Tool 3: [Nome da Ferramenta]

**Descrição**: O que esta ferramenta faz.

**Parâmetros**:
- `param1` (array, obrigatório): Descrição
- `param2` (object, opcional): Descrição

**Retorno**: Descrição do que a ferramenta retorna.

**Exemplo de Uso**:
```json
{
  "tool": "tool3",
  "parameters": {
    "param1": ["item1", "item2"]
  }
}
```

## Boas Práticas

- Use as ferramentas de forma eficiente
- Sempre valide os parâmetros antes de chamar
- Trate os erros adequadamente
- Documente qualquer uso personalizado
