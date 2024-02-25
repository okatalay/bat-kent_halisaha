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

def sql_delete(table, value1, value2):

    try:
        vt = sql.connect('batikent.sqlite')
        cursor = vt.cursor()
        cursor.execute(f"DELETE FROM {table} WHERE isim='{value1}' AND tel='{value2}'")
        vt.commit()

    except sql.Error as e:
        print("SQL_DELETE SORUNU:", e)

    finally:
        if vt:
            vt.close()

def sql_query(table, value1=None, value2=None):


        try:
            vt = sql.connect('batikent.sqlite')
            cursor = vt.cursor()

            if table == "rehber":

                cursor.execute(f"SELECT * FROM {table}")
                results = cursor.fetchall()

                return results

            elif table == "takvim":

                cursor.execute(f"SELECT * FROM takvim WHERE tarih BETWEEN '{value1}' AND '{value2}' ORDER BY tarih ASC")
                results = cursor.fetchall()

                return results

            elif table == "kullanici":

                cursor.execute(f"SELECT * FROM kullanici WHERE id='{value1}' AND sifre='{value2}'")
                results = cursor.fetchall()

                return results


        except sql.Error as e:
            print("SQL_SORGU SORUNU:", e)

        finally:
            if vt:
                vt.close()

