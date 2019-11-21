import psycopg2


def delete():
    con = psycopg2.connect(host='localhost', port='5432', user='postgres', password='postgres', dbname='postgres')
    cur = con.cursor()
    cur.execute("DELETE from postgres.public.pitter_user where id='1';")
    con.commit()

