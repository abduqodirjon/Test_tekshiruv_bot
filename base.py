import sqlite3

# c.execute("""CREATE TABLE customer (
#     fio text,
#     variant text,
#     t_javob int,
#     x_javob int,
#     sana text
#     )""")
# c.execute(""" INSERT INTO customer VALUES('Qodirjon', 'TTT-256', 27, 3, '2021-11-06')""")

def qaydnoma(txt):
    con = sqlite3.connect('customer.db')
    c = con.cursor()
    c.execute(" INSERT INTO customer VALUES(?, ?, ?, ?, ?)", txt)
    con.commit()
    con.close()

def ism_view(txt):
    con = sqlite3.connect('customer.db')
    c = con.cursor()
    c.execute(f'SELECT*FROM customer WHERE fio = "{txt}" ')
    t = c.fetchall()
    con.commit()
    con.close()
    return t

def variant_view(txt):
    con = sqlite3.connect('customer.db')
    c = con.cursor()
    c.execute(f'SELECT*FROM customer WHERE variant = "{txt}" ORDER BY t_javob DESC')
    t = c.fetchall()
    con.commit()
    con.close()
    return t

def ismni_tek(txt, txt_v):
    con = sqlite3.connect('customer.db')
    c = con.cursor()
    c.execute(f'SELECT*FROM customer WHERE fio = "{txt}" ORDER BY variant DESC')
    t = c.fetchall()
    if len(t)==0:
        return False
    else:
        for item in t:
            if txt_v == item[1]:
                return True
            
    con.commit()
    con.close()
    return False
