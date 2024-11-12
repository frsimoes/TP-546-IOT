import network
import utime
import credenciais
 
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(credenciais.ssid,credenciais.senha)
 
# Espera por até 10 segundos pela conexão Wi-Fi
wait = 10
while wait > 0:
  if wlan.status() < 0 or wlan.status() >= 3:
    break
  wait -= 1
  print('aguardando conexao...')
  utime.sleep(1)
 
# Verifica o status da conexão após a espera
if wlan.status() != 3:
  raise RuntimeError('a conexao falhou')
else:
  print('conectado')
  print('IP: ', wlan.ifconfig()[0])
