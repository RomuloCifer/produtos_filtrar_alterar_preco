produtos = [
    {'nome': 'Camiseta', 'preco': 50},
    {'nome': 'Calça Jeans', 'preco': 120},
    {'nome': 'Tênis', 'preco': 300},
    {'nome': 'Boné', 'preco': 40},
    {'nome': 'Relógio', 'preco': 250},
    {'nome': 'Mochila', 'preco': 150},
    {'nome': 'Jaqueta', 'preco': 350},
    {'nome': 'Óculos de Sol', 'preco': 200},
    {'nome': 'Meias', 'preco': 20},
    {'nome': 'Carteira', 'preco': 80},
]
import pprint
def filtrar_por_preco(mm):
    
        if mm == '>':
            valor = input('Valores maiores a que?')
            valor = float(valor)
            return verificar_itens_maior(produtos,valor)
        elif mm == '<':
            valor = input('Valores menores a que?')
            valor = float(valor)
            return verificar_itens_menor(produtos,valor)     
            
   

def verificar_itens_maior(lista,valor):
    verificar_lista =[
    {**item} for item in lista if item['preco'] > valor
    ]
    #print(verificar_lista)
    return verificar_lista

def verificar_itens_menor(lista,valor):
    verificar_lista =[
    {**item} for item in lista if item['preco'] < valor
    ]
    #print(verificar_lista)
    return verificar_lista

def aplicar_valores_novos(lista, desconto_aumento,porcentagem_desconto):
    produtos_preco_alterado = []
    for produto in lista:
        preco_atual = produto['preco']
        if desconto_aumento == 'd':
            novo_preco = produto['preco'] * (1 - porcentagem_desconto / 100)
            novo_produto = {**produto, 'preco': round(novo_preco, 2)}
            produtos_preco_alterado.append(novo_produto)

        
        elif desconto_aumento == 'a':
            novo_preco = produto['preco'] * (1 + porcentagem_desconto / 100)
            novo_produto = {**produto, 'preco': round(novo_preco, 2)}
            produtos_preco_alterado.append(novo_produto)
    return produtos_preco_alterado


# exibir os produtos disponiveis
print('Produtos disponíveis para alteração.')
lista_produtos = []
for produto in produtos:
   lista_produtos.append(produto['nome'])
lista_produtos.sort()

for i in range(len(lista_produtos)):
    print (lista_produtos[i].ljust(20), end='')
    if (i + 1) % 5 == 0:
        print()


#pergunta ao usuario se ele deseja ver os valores maiores ou menores
continuar = True
#fazer isso dentro da funcao de vericiar itens
while continuar:
    verificar_preco_usuario = input("Deseja ver valores maiores '>'' ou menores? '<': ")
    if verificar_preco_usuario in ('>', '<'):
        continuar =  False
    else:
        print("Digite uma chave válida. '>' ou '<'")
listar_por_preco = filtrar_por_preco(verificar_preco_usuario)

print(listar_por_preco)

#pergunta se quer aplicar desconto ou aumentar o preço

desconto_ou_aumentar = input('Deseja aumentar ou diminuir o preço? \n' \
'[a]umentar [d]esconto')
while True:
    porcentagem_desc_aume = input('De quantos por cento?')
    porcentagem_desc_aume = int(porcentagem_desc_aume)
    if porcentagem_desc_aume > 100:
        print('Desconto máximo de 100%')
    elif porcentagem_desc_aume < 0:
        print('Digite um valor maior que 0')
    else:
        break
produtos_alterados = aplicar_valores_novos(listar_por_preco,desconto_ou_aumentar,porcentagem_desc_aume)


print(produtos_alterados)

# tratar listas vazias
#quando o usuario nao coloca >< continua para a proxima pergunta de qualquer jeito
#talvez perguntar se deseja sair