import psutil
import time

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

time.sleep(3)