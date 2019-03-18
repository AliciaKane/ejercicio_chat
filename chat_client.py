import socket

IP = "10.108.33.41"
PORT = 8024


# create an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(serversocket)

def process_server(serversocket):
    intento = True
    while intento:
        mensaje_cliente = str(input("Cliente: "))
        mensaje_bytes = str.encode(mensaje_cliente)
        serversocket.send(mensaje_bytes)
        mensaje_recibido = serversocket.recv(2048).decode("utf-8")
        print(mensaje_recibido)
        if mensaje_recibido == "salir" or mensaje_recibido == "Salir" or mensaje_recibido == "SALIR":
            serversocket.close()
            intento = False
try:
    serversocket.connect((IP, PORT))
    process_server(serversocket)

except OSError:
    print("Socket already used")
    # But first we need to disconnect
    serversocket.close()
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.connect((IP, PORT))
