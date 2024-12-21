import socket
import threading

# Configuración inicial
HOST = '127.0.0.1'
PORT = 65432
MAX_SEATS = 50
seat_prices = 5000
seats_sold = []

# Manejo de conexiones
def handle_client(client_socket):
    global seats_sold
    try:
        while True:
            request = client_socket.recv(1024).decode('utf-8')
            if request.startswith("BUY"):
                _, num_seats = request.split()
                num_seats = int(num_seats)

                if num_seats > 5:
                    client_socket.sendall("ERROR: No puede comprar más de 5 entradas por petición.".encode('utf-8'))
                elif len(seats_sold) + num_seats > MAX_SEATS:
                    client_socket.sendall("ERROR: No hay suficientes asientos disponibles.".encode('utf-8'))
                else:
                    allocated_seats = list(range(len(seats_sold) + 1, len(seats_sold) + 1 + num_seats))
                    seats_sold.extend(allocated_seats)
                    total_price = num_seats * seat_prices
                    response = f"COMPRADO: Total={total_price}, Asientos={allocated_seats}"
                    client_socket.sendall(response.encode('utf-8'))
            elif request == "INFO":
                client_socket.sendall("Fecha: 31-12-2024, Hora: 20:00".encode('utf-8'))
            else:
                client_socket.sendall("ERROR: Comando desconocido.".encode('utf-8'))
    finally:
        client_socket.close()

# Servidor principal
def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)
    print("Servidor escuchando en {}:{}".format(HOST, PORT))

    while True:
        client_socket, addr = server.accept()
        print("Conexión aceptada desde:", addr)
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    main()
