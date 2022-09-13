import psycopg2 as pg

con = pg.connect(host='localhost', database='Library', user='postgres', password='Ellen@2023')
print("Conectado")

sql = con.cursor()
sql.execute("SELECT * FROM books")
query = sql.fetchall()

for res in query:
    print(res)

sql_insert = "INSERT INTO books (bk_id, bk_name, bk_author)" \
             "VALUES (8, 'The Lord of the Rings: The Fellowshipofthe Ring', 'J. R. R. Tolkien')," \
                    "(9, 'The Lord of the Rings: The Two Towers', 'J. R. R. Tolkien')," \
                    "(10, 'The Lord of the Rings: The Return of the King', 'J. R. R. Tolkien')"
sql.execute(sql_insert)
con.commit()

sql.execute("SELECT * FROM books")
query = sql.fetchall()

for res in query:
    print(res)

con.close()