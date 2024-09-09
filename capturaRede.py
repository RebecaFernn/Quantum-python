import psutil
import time
from mysql.connector import connect, Error
from dotenv import load_dotenv
import os

load_dotenv()

config = {
    'user': os.getenv("DB_USER"),
    'password': os.getenv("DB_PASSWD"),
    'host': os.getenv("DB_HOST"),
    'database': os.getenv("DB"),
}

pacotesTotal = 0
pacotesPerdidos = 0
perdaPorcentagem = 0

i = 0
while i < 5:
     rede = psutil.net_io_counters()
    #  pacotes recebidos que foram perdidos
     dropin = rede.dropin
    #  pacotes enviados que foram perdidos
     dropout = rede.dropout
     pacotesEnviado = rede.packets_sent
     pacotesRecebido = rede.packets_recv
     
     pacotesTotal += pacotesEnviado + pacotesRecebido
     pacotesPerdidos += dropin + dropout
     
     print(f"{i + 1} - Pacotes Enviados: ", pacotesEnviado)
     print(f"{i + 1} - Pacotes Recebidos: ", pacotesRecebido)
      
     i += 1
     time.sleep(3)
     
if pacotesPerdidos > 0:    
    perdaPorcentagem = (pacotesPerdidos / pacotesTotal) * 100 
else:
    perdaPorcentagem = 0
    
print("Pacotes Total: ", pacotesTotal)
print("Porcentagem de Perda: {:.2f}%".format(perdaPorcentagem))

if perdaPorcentagem >= 2:
    print("ALERTA! Perdas altas de pacotes: {:.2f}%".format(perdaPorcentagem))
    try:
        db = connect(**config)
        if db.is_connected():
         db_info = db.get_server_info()
         print('Connected to MySQL server version - \n', db_info)
         
         with db.cursor() as cursor:
             query = ("INSERT INTO registro VALUES "
                     "(null, current_timestamp(), 'Perdas alta de pacote', %s)")
             value = [perdaPorcentagem]
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


     
    
     
     