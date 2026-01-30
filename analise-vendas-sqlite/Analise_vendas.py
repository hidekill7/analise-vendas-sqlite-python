import sqlite3

# conecta ao banco
conexao = sqlite3.connect("vendas.db")
cursor = conexao.cursor()

# 1) Faturamento total
cursor.execute("""
SELECT SUM(quantidade * preco)
FROM vendas
""")
faturamento_total = cursor.fetchone()[0]

# 2) Produto mais vendido
cursor.execute("""
SELECT produto, SUM(quantidade) AS total_vendido
FROM vendas
GROUP BY produto
ORDER BY total_vendido DESC
LIMIT 1
""")
produto_mais_vendido = cursor.fetchone()

# 3) Faturamento por categoria
cursor.execute("""
SELECT categoria, SUM(quantidade * preco)
FROM vendas
GROUP BY categoria
""")
faturamento_categoria = cursor.fetchall()

conexao.close()

# Exibindo resultados
print(f"Faturamento total: R$ {faturamento_total:.2f}")
print(f"Produto mais vendido: {produto_mais_vendido[0]} ({produto_mais_vendido[1]} unidades)")

print("\nFaturamento por categoria:")
for categoria, valor in faturamento_categoria:
    print(f"- {categoria}: R$ {valor:.2f}")

