import socket  #biblioteca para comunicación de red
import threading  #manejo de hilos para concurrencia
import random  #selección aleatoria (para determinar perdedores)
import time  #introducir retrasos en la ejecución

#configuración del servidor
HOST = '127.0.0.1'  #dirección IP local
PORT = 65433  #puerto de conexion
MAX_PLAYERS = 3  #número máximo de jugadores permitidos en una partida
players = []  #lista que almacena los jugadores activos    

#Maneja el juego en sí
def handle_game():
    global players #accede a los jugadores globalmente
    while True:
        if len(players) == MAX_PLAYERS: #solo se puede jugar de a tres
            print("Jugadores actuales:")
            for i in range(0,3):    
                print("Jugador:", players[i]["name"])  #mostramos quienes estan involucrados en la partida
            print("jugando...")
            time.sleep(8)
            loser = random.choice(players) #el perdedor se escoge aleatoriamente
            print(f"Jugador {loser} pierde y abandona el juego.") #se anuncia el perdedor
            players.remove(loser) #lo quitamos de la lista de jugadores
        else:
            print("Esperando a que se unan más jugadores...") #mensaje periodico de espera hasta la proxima partida
            time.sleep(3) #periodicidad de 3 segundos

#Maneja el ingreso de jugadores
def ingreso(server):
    global players
    nombres = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"] #lista de nombres posibles
    while True:
        data, addr = server.recvfrom(1024) #espera recibir datos desde un cliente
        message = data.decode('utf-8') #decodifica los datos recibidos
        if len(players)!=3:
            if message == "JOIN": #mensaje de union desde un cliente
                if addr not in [player["addr"] for player in players]:  #verifica si el jugador se encuentra registrado
                    if len(nombres)>0:  #verifica si hay nombres disponibles
                        nombre_jugador = nombres[0]  #asigna el siguiente nombre disponible
                        nombre_jugador = nombres.pop(0) #eliminamos el nombre de la lista para que de la proxima vez que se juegue no se repita
                        players.append({"addr": addr, "name": nombre_jugador}) #agregamos el jugador a la lista de jugadores con su id y nombre a la lista
                        server.sendto(f"UNIDO COMO JUGADOR {nombre_jugador}".encode('utf-8'), addr) #envía una confirmación al cliente diciendo que se unió 
                        print(f"Jugador {nombre_jugador} unido desde {addr}.") #mostramos en el servidor el jugador ingresado
                    else:
                        server.sendto("NO HAY_MAS NOMBRES DISPONIBLES".encode('utf-8'), addr) #apartado de errores si ya no quedan nombres disponibles
                else:
                    server.sendto("YA ESTAS EN EL JUEGO".encode('utf-8'), addr) #error si el jugador ya está dentro del juego
            else:
                server.sendto("COMANDO NO RECONOCIDO".encode('utf-8'), addr) #error si no se ingresa el JOIN para entrar a jugar
        else:
            server.sendto("LA PARTIDA ESTA COMPLETA, ESPERE A QUE TERMINE".encode('utf-8'), addr)

#Control principal del servidor
def main():
    global players #lista de player manipulada globalmente
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #crea un socket Datagram con protocolo UDP para manejar los datagramas
    server.bind((HOST, PORT)) #asocia el socket al host y puerto configurados
    print("Servidor de juego iniciado.")

    #Inicia el hilo para manejar el juego
    game_thread = threading.Thread(target=handle_game, daemon=True) #crea un hilo para la lógica del juego
    game_thread.start() #inicia el hilo del juego

    #Maneja continuamente las solicitudes de ingreso
    ingreso(server)


if __name__ == "__main__":
    main()