# Sistema de Filtro e Alteração de Preços

Sistema em Python para filtrar produtos por preço e aplicar alterações em massa nos valores.

## Funcionalidades

- Lista todos os produtos disponíveis
- Filtra produtos por preço (maior ou menor que um valor)
- Permite aplicar desconto ou aumento percentual nos preços
- Exibe resultado com preços atualizados
- Validação de entradas do usuário

## Como usar

1. Execute o script Python
2. Visualize a lista de produtos disponíveis
3. Escolha filtrar por valores maiores (>) ou menores (<) que um valor específico
4. Insira o valor de referência para o filtro
5. Escolha entre aplicar desconto (d) ou aumento (a)
6. Insira a porcentagem desejada (1-100)
7. Visualize os resultados com os preços atualizados

## Exemplo de uso

```python
Produtos disponíveis para alteração.
Boné                Camiseta            Carteira            Jaqueta             Meias
Mochila             Óculos de Sol       Relógio            Tênis               

Deseja ver valores maiores '>' ou menores? '<': >
Valores maiores a que? 100

Deseja aumentar ou diminuir o preço?
[a]umentar [d]esconto: d
De quantos por cento? 10
```

## Requisitos

- Python 3.x

## Estrutura do projeto

- `produtos_filtrar_preco.py`: Script principal com toda a lógica do sistema
- `README.md`: Documentação do projeto
