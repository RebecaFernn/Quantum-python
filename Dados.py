import psutil
import time


contador = 1
i = 0
while i < contador: 
    cpu_percent = psutil.cpu_percent()
    memory = psutil.virtual_memory()
    disk_usage = psutil.disk_usage("/")
    print(f"Uso de memória: {memory.percent}%")
    print(f"Uso de disco: {disk_usage.percent}%")
    print(f"Uso da CPU: {cpu_percent}%")
    print("-------------------------------------")
    time.sleep(5)
    
