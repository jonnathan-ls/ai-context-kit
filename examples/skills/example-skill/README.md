# Example Skill: Processador de Texto

## Descrição

Uma skill de exemplo que demonstra como processar texto de entrada e retornar uma versão modificada.

## Configuração

```json
{
  "name": "text-processor",
  "version": "1.0.0",
  "description": "Processa texto aplicando transformações",
  "author": "Example Author",
  "category": "text-processing"
}
```

## Instruções

Esta skill recebe um texto como entrada e aplica as seguintes transformações:
1. Remove espaços extras
2. Converte para o formato desejado
3. Retorna o texto processado

## Exemplos

### Exemplo 1: Normalização de Texto

**Entrada**:
```
Texto   com    espaços    extras
```

**Saída**:
```
Texto com espaços extras
```

### Exemplo 2: Conversão de Caso

**Entrada**:
```
texto em minúsculas
```

**Saída (uppercase)**:
```
TEXTO EM MINÚSCULAS
```

## Notas

- Esta é uma skill de exemplo para demonstração
- Pode ser adaptada para necessidades específicas
- Suporta múltiplos tipos de transformações
