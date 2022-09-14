import psycopg2 as pg

# Conexão com o banco de dados
con = pg.connect(host='localhost', database='Library', user='postgres', password='Ellen@2023')
print("Conectado")

sql = con.cursor()

# Inserindo informações no banco de dados
sql_insert = "INSERT INTO books (bk_id, bk_name, bk_author)" \
             "VALUES (8, 'The Lord of the Rings: The Fellowshipofthe Ring', 'J. R. R. Tolkien')," \
                    "(9, 'The Lord of the Rings: The Two Towers', 'J. R. R. Tolkien')," \
                    "(10, 'The Lord of the Rings: The Return of the King', 'J. R. R. Tolkien')"
sql.execute(sql_insert)
con.commit()

# Atualizando informações já existentes no banco de dados
sql_update = "UPDATE books SET bk_name = 'The Lord of the Rings: The Fellowship of the Ring' WHERE bk_id = 8"
sql.execute(sql_update)
con.commit()

# Deletando informações do banco de dados
sql_delete = "DELETE FROM books WHERE bk_id = 10"
sql.execute(sql_delete)
con.commit()

# Lendo informações do banco de dados
sql.execute("SELECT * FROM books")
query = sql.fetchall()

for res in query:
    print(res)

con.close()