
import sqlite3 as sql

def sql_query(table, value1=None, value2=None):
    try:
        vt = sql.connect('batikent.sqlite')
        cursor = vt.cursor()

        if table == "rehber" or table == "kullanici":

            cursor.execute(f"SELECT * FROM {table}")
            results = cursor.fetchall()

            return results

        elif table == "takvim":

            cursor.execute(f"SELECT * FROM takvim WHERE tarih BETWEEN '{value1}' AND '{value2}'")
            results = cursor.fetchall()

            return results

    except sql.Error as e:
        print("SQL_SORGU SORUNU:", e)

    finally:
        if vt:
            vt.close()



print(sql_query("takvim", "2024-02-19", "2024-02-25"))
