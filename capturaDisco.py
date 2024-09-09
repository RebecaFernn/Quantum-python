import psutil
import time
from mysql.connector import connect, Error
from dotenv import load_dotenv
import os

perUsado = psutil.disk_usage('/').percent
discolivre = psutil.disk_usage('/').free
discoUsado = psutil.disk_usage('/').used
discoTotal = psutil.disk_usage('/').total

def formatando(num: float) -> float:
    return round(num, 2)

def convertendoGB(retorno: int) -> float:
    calculo = retorno / (1024**3)
    return formatando(calculo)
    
print(f"Disco Usado: {convertendoGB(discoUsado)} ({perUsado}%)")
print(f"Disco Livre: {convertendoGB(discolivre)}")
print(f"Disco Total: {convertendoGB(discoTotal)}")

if perUsado >= 90:
    print("ALERTA! Disco ficando cheio!")
    load_dotenv()

    config = {
        'user': os.getenv("DB_USER"),
        'password': os.getenv("DB_PASSWD"),
        'host': os.getenv("DB_HOST"),
        'database': os.getenv("DB"),
    }
    db = None
    try:
        db = connect(**config)
        if db.is_connected():
         db_info = db.get_server_info()
         print('Connected to MySQL server version - \n', db_info)
         
         with db.cursor() as cursor:
             query = ("INSERT INTO registro VALUES "
                     "(null, current_timestamp(), 'Disco ficando cheio!', %s, '%')")
             value = [perUsado]
             cursor.execute(query, value)
             db.commit()
             print(cursor.rowcount, "registro inserido")
         cursor.close()
    except Error as e:
        print('Error to connect with MySQL -', e)  
             
    finally:
        if db is not None and db.is_connected():
            cursor.close()
            db.close()
            print("MySQL connection is closed")
