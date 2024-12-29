import socket  #biblioteca para comunicación de red

HOST = '127.0.0.1' #dirección IP del servidor al que se conectará el cliente
PORT = 65433 #puerto del servidor al que el cliente enviará datos

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #crea un socket Datagram con protocolo UDP para la comunicación con el servidor

    while True: #ciclo indefinido para enviar comandos al servidor
        command = input("Ingrese comando (JOIN): ") #solicita un comando al usuario
        client.sendto(command.encode('utf-8'), (HOST, PORT)) #codifica en el comando en formato UTF-8 antes de enviarlo al servidor
        response, _ = client.recvfrom(1024) #espera una respuesta del servidor
        print("Respuesta del servidor:", response.decode('utf-8')) #decodifica y muestra la repsuesta


#punto de entrada del programa
#solo ejecuta el main() si el archivo se ejecuta directamente
if __name__ == "__main__":
    main()