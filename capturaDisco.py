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

def horario() -> str:
    horarioInicio = time.time()
    horarioAtual = time.localtime(horarioInicio)
    horarioFormatado = time.strftime("%d/%m/%Y %H:%M:%S", horarioAtual)
    return horarioFormatado
    
print(f"Disco Usado: {convertendoGB(discoUsado)} ({perUsado}%) // Data: {horario()}")
print(f"Disco Livre: {convertendoGB(discolivre)} // Data: {horario()}")
print(f"Disco Total: {convertendoGB(discoTotal)} // Data: {horario()}")

time.sleep(1)