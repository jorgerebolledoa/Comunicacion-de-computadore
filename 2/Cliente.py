import socket

HOST = '127.0.0.1'
PORT = 65433

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        command = input("Ingrese comando (JOIN): ")
        client.sendto(command.encode('utf-8'), (HOST, PORT))
        response, _ = client.recvfrom(1024)
        print("Respuesta del servidor:", response.decode('utf-8'))

if __name__ == "__main__":
    main()
