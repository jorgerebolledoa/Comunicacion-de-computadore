import socket  # Biblioteca para manejar la comunicación en red
import threading  # Biblioteca para manejar múltiples hilos (conexiones simultáneas)

# Configuración inicial del servidor
HOST = '127.0.0.1'  # Dirección IP donde el servidor escuchará (localhost)
PORT = 65432        # Puerto en el que el servidor estará escuchando
MAX_SEATS = 50      # Número máximo de asientos disponibles para la venta
seat_prices = 5000  # Precio por asiento
seats_sold = []     # Lista para llevar el registro de los asientos vendidos

# Función para manejar la interacción con un cliente
def handle_client(client_socket):
    global seats_sold  # Permite modificar la lista de asientos vendidos
    try:
        while True:
            # Recibe y decodifica la solicitud del cliente
            request = client_socket.recv(1024).decode('utf-8')
            
            # Procesa solicitudes que empiezan con "BUY"
            if request.startswith("BUY"):
                _, num_seats = request.split()  # Extrae el número de asientos solicitados
                num_seats = int(num_seats)      # Convierte a entero

                # Valida la cantidad de asientos solicitados
                if num_seats > 5:
                    client_socket.sendall("ERROR: No puede comprar más de 5 entradas por petición.".encode('utf-8'))
                elif len(seats_sold) + num_seats > MAX_SEATS:
                    client_socket.sendall("ERROR: No hay suficientes asientos disponibles.".encode('utf-8'))
                else:
                    # Calcula y asigna los asientos disponibles
                    allocated_seats = list(range(len(seats_sold) + 1, len(seats_sold) + 1 + num_seats))
                    seats_sold.extend(allocated_seats)  # Actualiza la lista de asientos vendidos
                    total_price = num_seats * seat_prices  # Calcula el precio total
                    # Responde con los detalles de la compra
                    response = f"COMPRADO: Total={total_price}, Asientos={allocated_seats}"
                    client_socket.sendall(response.encode('utf-8'))

            # Procesa solicitudes de información general
            elif request == "INFO":
                client_socket.sendall("Fecha: 31-12-2024, Hora: 20:00".encode('utf-8'))

            # Maneja comandos desconocidos
            else:
                client_socket.sendall("ERROR: Comando desconocido.".encode('utf-8'))
    finally:
        # Cierra la conexión con el cliente al salir del bucle
        client_socket.close()

# Función principal del servidor
def main():
    # Crea un socket para el servidor usando IPv4 (AF_INET) y TCP (SOCK_STREAM)
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))  # Asocia el socket a la dirección y puerto configurados
    server.listen(5)          # Escucha hasta 5 conexiones simultáneas en cola
    print("Servidor escuchando en {}:{}".format(HOST, PORT))

    # Bucle principal del servidor
    while True:
        # Acepta una nueva conexión
        client_socket, addr = server.accept()
        print("Conexión aceptada desde:", addr)
        
        # Crea un nuevo hilo para manejar la conexión del cliente
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()  # Inicia el hilo

# Ejecuta la función principal si este archivo se ejecuta como un programa
if __name__ == "__main__":
    main()
