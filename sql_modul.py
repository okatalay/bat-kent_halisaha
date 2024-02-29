import sqlite3 as sql

def sql_into(table, entry_values):

    try:
        vt = sql.connect('C:/PROJELER/BATIKENT/batikent.sqlite')
        cursor = vt.cursor()
        cursor.execute(f"INSERT INTO {table} VALUES ({','.join(['?' for _ in range(len(entry_values))])})", entry_values)
        results = cursor.fetchall()
        vt.commit()

    except sql.Error as e:
        print("SQL_INTO SORUNU:", e)

    finally:
        if vt:
            vt.close()

def sql_delete(table, value1, value2):

    try:
        vt = sql.connect('C:/PROJELER/BATIKENT/batikent.sqlite')
        cursor = vt.cursor()
        cursor.execute(f"DELETE FROM {table} WHERE isim='{value1}' AND tel='{value2}'")
        vt.commit()

    except sql.Error as e:
        print("SQL_DELETE SORUNU:", e)

    finally:
        if vt:
            vt.close()
def sql_query(table, column1="*", column2=None, value2=None):

    if column1 != "*":

        try:
            connect = sql.connect('C:/PROJELER/BATIKENT/batikent.sqlite')
            vt = connect
            cursor = vt.cursor()

            cursor.execute(f"SELECT {column1} FROM {table} WHERE {column2}='{value2}'")
            #cursor.execute(f"SELECT * FROM ydk_liste WHERE adi='{value1}' AND sifre='{value2}'")
            results = cursor.fetchall()

            return results

        except sql.Error as e:
            print("SQL_SORGU SORUNU:", e)

        finally:
            if vt:
                vt.close()

    else :

        try:
            connect = sql.connect('C:/PROJELER/BATIKENT/batikent.sqlite')
            vt = connect
            cursor = vt.cursor()

            cursor.execute(f"SELECT * FROM {table} WHERE {column2}='{value2}'")
            # cursor.execute(f"SELECT * FROM ydk_liste WHERE adi='{value1}' AND sifre='{value2}'")
            results = cursor.fetchall()

            return results

        except sql.Error as e:
            print("SQL_SORGU SORUNU:", e)

        finally:
            if vt:
                vt.close()
def sql_query_all(table,column=None):


    try:
        vt = sql.connect('C:/PROJELER/BATIKENT/batikent.sqlite')
        cursor = vt.cursor()

        if column is None:

            cursor.execute(f"SELECT * FROM '{table}'")
            # cursor.execute(f"SELECT * FROM ydk_liste WHERE adi='{value1}' AND sifre='{value2}'")
            results = cursor.fetchall()
        else:

            cursor.execute(f"SELECT {column} FROM '{table}'")
            results = cursor.fetchall()

        return results

    except sql.Error as e:
        print("SQL_SORGU SORUNU:", e)

    finally:
        if vt:
            vt.close()