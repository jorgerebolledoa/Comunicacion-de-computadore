import socket

HOST = '127.0.0.1'
PORT = 65432

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    while True:
        command = input("Ingrese comando (BUY <num_asientos>/INFO): ")
        client.sendall(command.encode('utf-8'))
        response = client.recv(1024).decode('utf-8')
        print("Respuesta:", response)

if __name__ == "__main__":
    main()
