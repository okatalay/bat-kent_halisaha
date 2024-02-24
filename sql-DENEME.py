import sqlite3 as sql

def sql_into(table, value1, value2):

    try:
        vt = sql.connect('batikent.sqlite')
        cursor = vt.cursor()
        cursor.execute(f"INSERT INTO {table} VALUES ('{value1}', '{value2}')")
        results = cursor.fetchall()
        vt.commit()

    except sql.Error as e:
        print("SQL_INTO SORUNU:", e)

    finally:
        if vt:
            vt.close()



