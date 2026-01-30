import sqlite3

# cria ou conecta ao banco
conexao = sqlite3.connect("vendas.db")
cursor = conexao.cursor()

# cria a tabela
cursor.execute("""
CREATE TABLE IF NOT EXISTS vendas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    produto TEXT,
    categoria TEXT,
    quantidade INTEGER,
    preco REAL,
    data TEXT
)
""")

# inserindo dados de exemplo
dados = [
    ("Pão", "Alimentos", 10, 1.50, "2026-01-10"),
    ("Leite", "Bebidas", 5, 4.20, "2026-01-11"),
    ("Café", "Bebidas", 3, 8.90, "2026-01-11"),
    ("Bolo", "Alimentos", 2, 15.00, "2026-01-12")
]

cursor.executemany("""
INSERT INTO vendas (produto, categoria, quantidade, preco, data)
VALUES (?, ?, ?, ?, ?)
""", dados)

conexao.commit()
conexao.close()

print("Banco criado e dados inseridos com sucesso!")

