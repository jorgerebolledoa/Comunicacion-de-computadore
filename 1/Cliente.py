import socket  # Importa la biblioteca de sockets para permitir comunicación en red

# Define la dirección del servidor al que se conectará el cliente
HOST = '127.0.0.1'  # Dirección IP del servidor (localhost)
PORT = 65432        # Puerto en el que el servidor está escuchando

# Función principal del programa
def main():
    # Crea un socket para la comunicación usando IPv4 (AF_INET) y TCP (SOCK_STREAM)
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Establece una conexión al servidor en la dirección y puerto definidos
    client.connect((HOST, PORT))

    # Bucle principal para interactuar con el servidor
    while True:
        # Solicita al usuario que ingrese un comando
        command = input("Ingrese comando (BUY <num_asientos>/INFO): ")
        
        # Envía el comando al servidor, codificado como UTF-8
        client.sendall(command.encode('utf-8'))
        
        # Recibe la respuesta del servidor, con un máximo de 1024 bytes, y la decodifica
        response = client.recv(1024).decode('utf-8')
        
        # Imprime la respuesta del servidor en la consola
        print("Respuesta:", response)

# Ejecuta la función principal si este archivo se ejecuta como un programa
if __name__ == "__main__":
    main()
