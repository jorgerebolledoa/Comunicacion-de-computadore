import socket
import threading
import random

HOST = '127.0.0.1'
PORT = 65433
MAX_PLAYERS = 3
players = []

def handle_game():
    global players
    while len(players) > 1:
        print("Jugadores actuales:", players)
        loser = random.choice(players)
        print(f"Jugador {loser} pierde y abandona el juego.")
        players.remove(loser)

        if len(players) < MAX_PLAYERS:
            print("Esperando más jugadores...")
    print("Juego terminado.")

def main():
    global players
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind((HOST, PORT))
    print("Servidor de juego iniciado.")

    while len(players) < MAX_PLAYERS:
        data, addr = server.recvfrom(1024)
        message = data.decode('utf-8')
        if message == "JOIN":
            if addr not in players:
                players.append(addr)
                server.sendto("UNIDO".encode('utf-8'), addr)
            else:
                server.sendto("YA_ESTAS_EN_EL_JUEGO".encode('utf-8'), addr)

    game_thread = threading.Thread(target=handle_game)
    game_thread.start()

if __name__ == "__main__":
    main()
