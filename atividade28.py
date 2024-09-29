# Crie um programa que receba uma lista com o nome de 5 produtos e outra lista com as quantidades em estoque de cada um desses produtos. O programa deve exibir os produtos que estão com o estoque zerado.

# Exemplo de entrada:
# Produtos: ['Arroz', 'Feijão', 'Macarrão', 'Açúcar', 'Sal']
# Estoque: [10, 0, 5, 0, 20]

# Exemplo de saída:
# Produtos com estoque zerado: Feijão, Açúcar

produtos = []
estoque = []

for cont in range(5):
    produto = input('Digite o nome de um produto: ')
    quant_estoque = int(input('Digite o estoque do produto: '))
    produtos.append(produto)
    estoque.append(quant_estoque)

produtos_estoque_zerado = []
for i in range(5):
    if estoque [i] == 0:
        produtos_estoque_zerado.append(produtos[i])

if produtos_estoque_zerado:
    print('Produtos com estoque zerado:', ','.join(produtos_estoque_zerado))
else:
    print('Não há produtos com estoque zerado')
    
