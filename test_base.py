
from os import extsep
import sqlite3
import datetime
vaqt = datetime.datetime.now().strftime("%x")

# c.execute("""CREATE TABLE testlar (
#     variant text,
#     t_javob text,
#     sana text,
#     holat text      
#     )""")


# c.execute(""" INSERT INTO testlar VALUES('GQQ', 'abcdabcdac', '2021-11-06', 'ochiq')""")
# c.execute("DROP TABLE customer")

def test_ochish(txt_1, txt_2):
    con = sqlite3.connect("testlar.db")
    c = con.cursor()
    txt = (f"{txt_1}", f"{txt_2}", f"{vaqt}", "yopiq")
    c.execute(" INSERT INTO testlar VALUES(?, ?, ?, ?)", txt)
    con.commit()
    con.close()
def test_holati(txt):
    con = sqlite3.connect("testlar.db")
    c = con.cursor()
    c.execute(f'SELECT*FROM testlar WHERE variant = "{txt}"')
    t = c.fetchall()
    if len(t)>0:
        con.commit()
        con.close()
        return t[0][3]
    else:
        con.commit()
        con.close()
        return "none"
    
def test_yopish(txt):
    con = sqlite3.connect("testlar.db")
    c = con.cursor()
    info = ""
    c.execute(f'SELECT*FROM testlar WHERE variant = "{txt}"')
    t = c.fetchone()
    try:
        if t[3]=='yopiq':
            c.execute(f'UPDATE testlar SET holat = "ochiq" WHERE variant = "{txt}"')
            info = f"{txt} - variantli test <b>Ochildi 📫</b>\nNima qilishni quyidagi tugmalardan tanlang 👇"         
        elif t[3]=='ochiq':
            c.execute(f'UPDATE testlar SET holat = "yopiq" WHERE variant = "{txt}"')
            info = f"{txt} - variantli test <b>Yopildi 📫</b>\nNima qilishni quyidagi tugmalardan tanlang 👇"
    except:
        info = f"{txt} - variantli test topilmadi 🤷🏻‍♂️"
    con.commit()
    con.close()
    return info
def variant_conf_admin(txt):
    con = sqlite3.connect("testlar.db")
    c = con.cursor()
    c.execute(f'SELECT*FROM testlar WHERE variant = "{txt}"')
    t = c.fetchall()
    if len(t)==0:
        info = True
    else:
        info = False
    con.commit()
    con.close()
    return info

def variant_conf(txt):
    con = sqlite3.connect("testlar.db")
    c = con.cursor()
    c.execute(f'SELECT*FROM testlar WHERE variant = "{txt}"')
    t = c.fetchall()
    if len(t)==0:
        info = False
    else:
        info = True
    con.commit()
    con.close()
    return info

def test_topshirish(txt):
    con = sqlite3.connect("testlar.db")
    c = con.cursor()
    info = ""
    try:
        c.execute(f'SELECT*FROM testlar WHERE variant = "{txt}"')
        t = c.fetchone()
        if len(t)!=0:
            if t[3]=="yopiq":
                info = f'"{txt}" - variantli test yopiq 🚷'
            else:
                return t
        else:
            info = f'Kechirasiz <b>"{txt}"</b> - varianti topilmadi 🤷🏻‍♂️'
    except:
        info = f'Kechirasiz <b>"{txt}"</b> - varianti topilmadi 🤷🏻‍♂️'
    con.commit()
    con.close()
    return info

def test_holati_user(txt):
    con = sqlite3.connect("testlar.db")
    c = con.cursor()
    c.execute(f'SELECT*FROM testlar WHERE variant = "{txt}"')
    t = c.fetchall()
    con.commit()
    con.close()
    info = True
    if len(t)>0:
       if t[0][3]=="ochiq":
          info = False
    else:
        return "none"
    return info


def var_tek(txt):
    con = sqlite3.connect("testlar.db")
    c = con.cursor()
    c.execute(f'SELECT*FROM testlar WHERE variant = "{txt}"')
    t = c.fetchall()
    con.commit()
    con.close()
    info = True
    if len(t)>0:
          info = False
    return info
