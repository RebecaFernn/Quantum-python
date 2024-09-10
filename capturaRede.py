import psutil
import time

pacotesTotal = 0
pacotesPerdidos = 0
perdaPorcentagem = 0

def horario() -> str:
    horarioInicio = time.time()
    horarioAtual = time.localtime(horarioInicio)
    horarioFormatado = time.strftime("%d/%m/%Y %H:%M:%S", horarioAtual)
    return horarioFormatado

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
     
     print(f"{i + 1} - Pacotes Enviados: {pacotesEnviado} // Data: {horario()}")
     print(f"{i + 1} - Pacotes Recebidos: {pacotesRecebido} // Data: {horario()}")
      
     i += 1
     time.sleep(2)
     
if pacotesPerdidos > 0:    
    perdaPorcentagem = (pacotesPerdidos / pacotesTotal) * 100 
else:
    perdaPorcentagem = 0
    
print("Pacotes Total: ", pacotesTotal)
print("Porcentagem de Perda: {:.2f}%".format(perdaPorcentagem))


     
     