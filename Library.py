import psycopg2 as pg

con = pg.connect(host='localhost', database='Library', user='postgres', password='Ellen@2023')

print("Conectado")

select = con.cursor()
select.execute("SELECT * FROM books")

query = select.fetchall()

for res in query:
    print(res)
