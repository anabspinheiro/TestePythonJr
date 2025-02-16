import pandas as pd 

dados = pd.read_csv('vendas.csv')

# Calcular o faturamento
dados['faturamento'] =dados['quantidade'] * dados['preco_unitario']
faturamento_por_produto = dados.groupby('produto')['faturamento'].sum()

# Identificar em faturamento maior e menor produto
prod_maior_faturamento = faturamento_por_produto.idxmax()
prod_menor_faturamento = faturamento_por_produto.idxmin()

print("Faturamento por produto:")
print(faturamento_por_produto)
print(f"\nProduto com maior faturamento: {prod_maior_faturamento}")
print(f"\Produto com menor faturamento: {prod_menor_faturamento}")