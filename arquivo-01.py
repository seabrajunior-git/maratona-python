# Arquivos 01
ips_validos = []
ips_invalidos = []

def testa_ip(ip):
  ip_teste = ip.split(".")
  if (int(ip_teste[0])> 255 or int(ip_teste[0])< 0) or (int(ip_teste[1])> 255 or int(ip_teste[1])< 0) or (int(ip_teste[2])> 255 or int(ip_teste[2])< 0) or (int(ip_teste[3])> 255 or int(ip_teste[3])< 0):
    ips_invalidos.append(ip)
  else:
    ips_validos.append(ip)

try:
  lista_ips = open("ips.txt","r")
except:
  print("Problemas ao ler o arquivo")
for ip in lista_ips:
  testa_ip(ip)

#gera novo arquivo
listas = open("lista_final","w")
listas.write("[Endereços válidos:]\n")
for item in ips_validos:
  listas.write(item)
listas.write("\n[Endereços inválidos:]\n")
for item in ips_invalidos:
  listas.write(item)
listas.close()
