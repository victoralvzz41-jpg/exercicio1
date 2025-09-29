# 4- Calculadora de Preço Total

# Definindo as informações da compra
nome_produto = "Cadeira Infantil"
preco_unitario = 12.40  # Preço por unidade
quantidade = 3

# Calculando o preço total
# Preço Total = Preço Unitário * Quantidade
preco_total = preco_unitario * quantidade

# Exibindo todas as informações e o resultado final
print("--- Detalhes da Compra ---")
print(f"Produto:        {nome_produto}")
print(f"Preço Unitário: R$ {preco_unitario:.2f}") # O ":.2f" formata o número para ter 2 casas decimais
print(f"Quantidade:     {quantidade}")
print("--------------------------")
print(f"Preço Total:    R$ {preco_total:.2f}")