import socket
from random import randint
PORT = 8024

IP = "10.108.33.41"
MAX_OPEN_REQUESTS = 5

repetir = True
def process_client(clientsocket):
    print("Se ha establecido conexion con:", clientsocket)
    print("Se ha creado una sala de chat")
    while repetir:
        recv_message = clientsocket.recv(2048).decode("utf-8")
        print(recv_message)
        if recv_message == "salir" or recv_message == "Salir" or recv_message == "SALIR":
            clientsocket.close()
            return

        send_message = str(input("Servidor: "))
        send_bytes = str.encode(send_message)
        clientsocket.send(send_bytes)

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
hostname = IP
try:
    serversocket.bind((hostname, PORT))
    serversocket.listen(MAX_OPEN_REQUESTS)

    while True:
        print("Waiting for connections at %s %i" % (hostname, PORT))
        (clientsocket, address) = serversocket.accept()
        process_client(clientsocket)

except socket.error:
    print("Problemas using port %i. Do you have permission?" % PORT)
